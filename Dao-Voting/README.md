**ApeXai DAO Simulation Server**  
This ApeXai service simulates a decentralized autonomous organization (DAO) voting process using weighted votes, returning structured outcomes for testing and education.

### Purpose  
The ApeXai DAO Simulation Server offers developers and learners a simple yet powerful tool to emulate DAO voting behavior. It helps test governance mechanisms or demonstrate how weighted voting can affect proposal outcomes.

### Usage  

**Requirements:**

- Python 3.7+
- FastAPI and Uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
```

Start the server with:

```bash
uvicorn apexai_dao_voting:app --host 0.0.0.0 --port 8001
```

Submit a GET request to `/apexai/dao/vote` with these parameters:

- `proposal_id`: Numeric identifier of the DAO proposal.
- `voter_weights`: A JSON-formatted dictionary mapping voter addresses to their voting weights.

**Example Request:**

```
http://localhost:8001/apexai/dao/vote?proposal_id=123&voter_weights={"0x123":0.6,"0x456":0.4}
```

### Sample Response  
```json
{
    "proposal_id": 123,
    "total_votes_for": 0.6,
    "total_votes_against": 0.4,
    "result": "Passed"
}
```
