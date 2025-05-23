**ApeXai Stablecoin APY Calculator**  
This ApeXai service estimates the annual percentage yield (APY) for stablecoin deposits based on the coin type, amount, lockup duration, and optionally, platform risk.

### Purpose  
The ApeXai Stablecoin APY Calculator offers users an intuitive way to project potential returns from stablecoin deposits within DeFi protocols. It's ideal for comparing options and optimizing yield strategies.

### Usage  

**Requirements:**

- Python 3.7+
- FastAPI and Uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
```

Launch the server using:

```bash
uvicorn apexai_stablecoin_apy:app --host 0.0.0.0 --port 8004
```

Send a GET request to `/apexai/defi/stablecoin_apy` with the following query parameters:

- `stablecoin_name`: Symbol of the stablecoin (e.g., USDT, USDC)
- `deposit_amount`: Amount of the stablecoin to deposit
- `lockup_period`: Lockup duration in days
- `platform_risk` (optional): Risk score of the deposit platform (0–1 scale)

**Example Request:**

```
http://localhost:8004/apexai/defi/stablecoin_apy?stablecoin_name=USDT&deposit_amount=1000&lockup_period=30&platform_risk=0.1
```

### Sample Response  
```json
{
    "stablecoin_apy": 0.025,
    "stablecoin_name": "USDT",
    "deposit_amount": 1000,
    "lockup_period": 30,
    "platform_risk": 0.1
}
```
