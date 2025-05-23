**ApeXai Risk Intelligence Server**  
This ApeXai module delivers a DeFi risk intelligence score derived from key input metrics including collateral ratio, asset liquidity, volatility, and optionally, market capitalization.

### Purpose  
ApeXai’s risk server enables users to evaluate DeFi positions by offering a clear, quantifiable risk score. This tool is designed to assist users in making better-informed investment decisions across decentralized financial platforms.

### Usage  

**Requirements:**

- Python 3.7+
- FastAPI and Uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
```

Start the server using:

```bash
uvicorn apexaidefi_risk:app --host 0.0.0.0 --port 8000
```

Query the API via a GET request at `/apexai/defi/risk` with these parameters:

- `collateral_ratio`: Ratio of collateral to loan value
- `liquidity`: Liquidity metric of the asset
- `volatility`: Asset's price volatility
- `market_cap` (optional): Asset's market capitalization

**Example Request:**

```
http://localhost:8000/apexai/defi/risk?collateral_ratio=0.8&liquidity=0.9&volatility=0.2&market_cap=1000000000
```

### Sample Response  
```json
{
    "risk_score": 65.23,
    "collateral_ratio": 0.8,
    "liquidity": 0.9,
    "volatility": 0.2,
    "market_cap": 1000000000
}
```
