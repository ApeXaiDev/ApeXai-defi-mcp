from fastapi import FastAPI, Query
from typing import Optional
import random

app = FastAPI(
    title="ApeXai DeFi Risk Intelligence",
    description="An ApeXai module that computes DeFi risk scores using financial input metrics.",
    version="1.0.0",
)

@app.get("/apexai/defi/risk")
async def get_defi_risk(
    collateral_ratio: float = Query(..., description="The collateral ratio of the DeFi position."),
    liquidity: float = Query(..., description="The liquidity of the underlying asset."),
    volatility: float = Query(..., description="The volatility of the underlying asset."),
    market_cap: Optional[float] = Query(None, description="The market capitalization of the underlying asset.")
):
    """
    Computes a DeFi risk score based on input metrics. This is a simplified risk model.
    """

    # Basic risk calculation (replace with a more sophisticated model)
    risk_score = (collateral_ratio * 0.4 + liquidity * 0.3 + volatility * 0.3) * random.uniform(0.5, 1.5)

    # Ensure the risk score is within a reasonable range
    risk_score = max(0, min(risk_score, 100))

    return {
        "risk_score": risk_score,
        "collateral_ratio": collateral_ratio,
        "liquidity": liquidity,
        "volatility": volatility,
        "market_cap": market_cap,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
