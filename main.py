import pandas as pd
from src.scorer import rank_candidates
from src.explain import explain

jobs = pd.read_csv("data/jobs.csv")
candidates = pd.read_csv("data/candidates.csv")

job_text = jobs.iloc[0]["description"]

ranked = rank_candidates(job_text, candidates)

ranked["reason"] = ranked.apply(lambda r: explain(job_text, r), axis=1)
ranked["rank"] = range(1, len(ranked) + 1)

out = ranked[["rank", "candidate_id", "name", "score", "reason"]]
out.to_csv("output/ranked_candidates.csv", index=False)

print(out)
