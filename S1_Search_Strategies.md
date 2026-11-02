# Supplement S1 — Literature search strategies

## PubMed — search strategies

**paired_explicit**
```
(urease[tiab]) AND ("jack bean"[tiab] OR "Canavalia ensiformis"[tiab] OR "plant urease"[tiab]) AND ("Helicobacter pylori"[tiab] OR "H. pylori"[tiab])
```

**h_pylori_urease**
```
(urease[tiab] OR "Urease"[Mesh]) AND (inhibit*[tiab] OR IC50[tiab] OR kinetics[tiab]) AND ("Helicobacter pylori"[tiab] OR "Helicobacter pylori"[Mesh])
```

**jack_bean_urease**
```
(urease[tiab] OR "Urease"[Mesh]) AND (inhibit*[tiab] OR IC50[tiab]) AND ("jack bean"[tiab] OR "Canavalia ensiformis"[tiab])
```

**comparative**
```
urease[tiab] AND (inhibitor*[tiab] OR inhibition[tiab]) AND (comparative[tiab] OR recombinant[tiab] OR "enzyme source"[tiab])
```

## Scopus — search strategy

```
TITLE-ABS-KEY(
  ("jack bean urease" OR "jackbean urease" OR "Canavalia ensiformis" OR "plant urease")
  AND ("Helicobacter pylori" OR "H. pylori" OR "bacterial urease")
  AND (inhibit* OR IC50 OR "half maximal inhibitory concentration" OR potency OR comparative)
)
```

PubMed and Scopus use platform-specific Boolean syntax and distinct query structures.

## Semantic Scholar — search strategies

| Query ID | Query |
|---|---|
| Q01_pair_jackbean_hp | `"jack bean" + "Helicobacter pylori" + urease` |
| Q02_pair_canavalia_hp | `"Canavalia ensiformis" + "Helicobacter pylori" + urease` |
| Q03_pair_jackbean_h_pylori | `"jack bean" + "H. pylori" + urease` |
| Q04_jackbean_inhibitors | `"jack bean urease" + inhibit*` |
| Q05_canavalia_inhibitors | `"Canavalia ensiformis" + inhibit* + urease` |
| Q06_plant_bacterial_assays | `"plant urease" + "bacterial urease" + inhibit*` |
| Q07_hp_inhibitors_broad | `"Helicobacter pylori" + urease + inhibit*` |

Search settings: `MAX_PER_QUERY=3000`; `PAGE_SIZE=1000`.

## Google Scholar — Publish or Perish recorded queries (17 October 2026)
Search expressions recorded for Publish or Perish searches:

```text
"jack bean urease" "Helicobacter pylori" inhibition
"jack bean" "H. pylori" urease "IC50"
"Canavalia ensiformis" "Helicobacter pylori" urease inhibitors
"urease" "jack bean" "H. pylori" comparative
"jack bean urease" "H. pylori urease" kinetics
"plant urease" "bacterial urease" inhibitors
```

Google Scholar contributed 31 identified records to the reported PRISMA total. These search expressions were recorded for searches conducted with Publish or Perish.

## Records identified by source
PubMed: 1,362; Scopus: 87; Google Scholar: 31; Semantic Scholar: 2,148. Total: 3,628 pre-deduplication search hits.
