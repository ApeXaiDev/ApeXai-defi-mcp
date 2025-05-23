from fastapi import FastAPI, Query
from typing import Dict
import random

app = FastAPI(
    title="ApeXai DAO Simulation",
    description="A simulation server from ApeXai that models DAO voting using weighted inputs.",
    version="1.0.0",
)

@app.get("/apexai/dao/vote")
async def get_vote_result(
    proposal_id: int = Query(..., description="The ID of the proposal being voted on."),
    voter_weights: Dict[str, float] = Query(
        ..., description="A dictionary of voter addresses and their corresponding voting weights."
    )
):
    """
    Simulates a DAO voting process and returns a result based on voting weights.
    """

    total_votes_for = 0
    total_votes_against = 0

    for voter, weight in voter_weights.items():
        if random.random() > 0.5:
            total_votes_for += weight
        else:
            total_votes_against += weight

    result = "Passed" if total_votes_for > total_votes_against else "Failed"

    return {
        "proposal_id": proposal_id,
        "total_votes_for": total_votes_for,
        "total_votes_against": total_votes_against,
        "result": result,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
