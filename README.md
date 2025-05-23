# ApeXai DeFi MCP Servers

This repository contains a collection of Model Context Protocol (MCP) servers for various DeFi use cases, built with FastAPI. These servers can be deployed on decentralized compute platforms such as 0G/Akash.

## What are MCPs and why are they valuable?

Model Context Protocols (MCPs) introduce a decentralized architecture that enables developers to create specialized servers delivering specific data and functionality to decentralized applications (dApps). Key benefits include:

*   **Improved Scalability:** Offload heavy computations and data processing to dedicated MCP servers, allowing dApps to scale efficiently.
*   **Enhanced Security:** MCP servers can run in secure enclaves, safeguarding sensitive computations and data from unauthorized access.
*   **Increased Flexibility:** Easily customize and update MCP servers to keep pace with evolving dApp requirements.
*   **Quantum-Safe Compute:** Configure MCPs with quantum-resistant cryptographic algorithms to future-proof dApps against quantum threats.

## MCPs in the ApeXai Ecosystem

These MCP servers are designed as core components of the ApeXai ecosystem. Deployable via the ApeXai marketplace, they empower dApp developers to access specialized DeFi data and logic—either for free or through rental models using the ApeXai token ($APEXAI). This ecosystem fosters developer monetization and rich dApp functionalities.

## MCP Servers

The following MCP servers are included in this repository:

*   **DeFi Risk:** Calculates a DeFi risk score from input parameters.
*   **DAO Voting:** Simulates DAO voting results based on voter weights.
*   **Stablecoin APY:** Computes APY for stablecoin deposits.

## Usage

To run any of these MCP servers locally:

1.  Ensure Python 3.7 or higher is installed.
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the desired server, e.g., for DeFi Risk:

    ```bash
    uvicorn apexai_defi_risk:app --host 0.0.0.0 --port 8000
    ```

Replace the module name (`apexai_defi_risk`) and port with the server you want to run. Refer to each server’s README for specific usage details.

## Deployment

These MCP servers are compatible with decentralized compute platforms like 0G and Akash. See the ApeXai documentation for deployment instructions and best practices.

## Contributing

Contributions to ApeXai MCP servers are highly encouraged. Please fork the repository and submit pull requests with improvements or new MCP servers.
