import requests

# Replace 'YOUR_API_KEY' with your actual Etherscan API key
api_key = 'YOUR_API_KEY'

# Ethereum address you want to query
eth_address = '0x742d35Cc6634C0532925a3b844Bc454e4438f44e3'  # Replace with the desired Ethereum address

# Define the Etherscan API URL
base_url = 'https://api.etherscan.io/api'
action = 'balance'  # The action to get the balance

# Construct the URL for the API request
url = f'{base_url}?module=account&action={action}&address={eth_address}&tag=latest&apikey={api_key}'

# Send the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Check if the API response contains the expected data
    if 'result' in data:
        balance_wei = int(data['result'])
        balance_ether = balance_wei / 10**18  # Convert Wei to Ether
        print(f'Balance of {eth_address}: {balance_ether} ETH')
    else:
        print('API response does not contain the expected data.')
else:
    print('API request failed with status code:', response.status_code)
