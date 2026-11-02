"""Analysis for paired JBU/HPU potency dataset (13 studies, 46 observations).
Requires numpy and scipy. Run: python S6_Analysis_13_Studies.py
"""
import csv
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy.stats import spearmanr

root = Path(__file__).resolve().parent
with (root / "S3_Paired_Potency_Data_46.csv").open(encoding="utf-8-sig", newline="") as fh:
    rows = list(csv.DictReader(fh))
a = np.array([float(r["JBU_uM"]) for r in rows], dtype=float)
b = np.array([float(r["HPU_uM"]) for r in rows], dtype=float)
ratios = b / a
assert len(rows) == 46 and np.all(a > 0) and np.all(b > 0)
groups = defaultdict(list)
for r in rows:
    groups[r["study_id"]].append(r)
assert len(groups) == 13
study_log_means = np.array([
    np.mean([np.log(float(r["HPU_uM"]) / float(r["JBU_uM"])) for r in rs])
    for rs in groups.values()
])
summary = {
    "n_studies": len(groups), "n_pairs": len(rows),
    "spearman": float(spearmanr(a, b).statistic),
    "observation_geometric_ratio": float(np.exp(np.mean(np.log(ratios)))),
    "equal_study_geometric_ratio": float(np.exp(np.mean(study_log_means))),
    "n_HPU_lower": int(np.sum(ratios < 1)),
}
# Bootstrap resamples independent studies, not individual observations.
rng = np.random.default_rng(20261101)
boot = np.exp(rng.choice(study_log_means, size=(10000, len(groups)), replace=True).mean(axis=1))
summary["study_bootstrap_CI_95"] = [float(x) for x in np.percentile(boot, [2.5, 97.5])]
# Study-level correlation of mean log10 concentrations.
study_pairs = [(
    np.mean([np.log10(float(r["JBU_uM"])) for r in rs]),
    np.mean([np.log10(float(r["HPU_uM"])) for r in rs])
) for rs in groups.values()]
summary["study_level_spearman"] = float(spearmanr([x for x, _ in study_pairs], [y for _, y in study_pairs]).statistic)
loo = []
for excluded in groups:
    retained = [r for r in rows if r["study_id"] != excluded]
    aa = np.array([float(r["JBU_uM"]) for r in retained])
    bb = np.array([float(r["HPU_uM"]) for r in retained])
    loo.append({"excluded_study": excluded, "n_pairs": len(retained), "n_studies": len(groups)-1,
        "spearman": float(spearmanr(aa, bb).statistic),
        "observation_geometric_ratio": float(np.exp(np.mean(np.log(bb / aa))))})
import json
print(json.dumps({"summary": summary, "leave_one_study_out": loo}, indent=2))