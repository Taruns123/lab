# To extract live data via Infura.io, you can use the `web3.py` library, which is a popular Python library for interacting with Ethereum. Infura provides a service that allows you to connect to Ethereum nodes easily. Here's a Python code snippet to get the latest block number as an example:

# 1. First, you need to install the `web3.py` library if you haven't already:

# ```bash
# pip install web3
# ```

# 2. Then, you can use the following Python code to connect to Infura.io and retrieve the latest block number:

# ```python
from web3 import Web3

# Replace with your Infura Project ID and Ethereum network (mainnet, ropsten, etc.)
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"

# Initialize a Web3 instance
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection to Infura is successful
if web3.isConnected():
    try:
        # Get the latest block number
        latest_block_number = web3.eth.blockNumber
        print(f'Latest block number: {latest_block_number}')
    except Exception as e:
        print(f'An error occurred: {e}')
else:
    print('Failed to connect to Infura.io')

# ```

# Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID. You can obtain the project ID by signing up on the Infura website and creating a project.

# In this code:

# - We import the `Web3` class from the `web3` library.
# - We initialize a `Web3` instance by providing the Infura URL for the Ethereum network you want to connect to.
# - We check if the connection is successful using `web3.isConnected()`.
# - If the connection is successful, we retrieve the latest block number using `web3.eth.blockNumber` and print it.

# You can adapt this code to perform other Ethereum-related tasks with Infura, such as sending transactions, querying balances, or retrieving transaction data.