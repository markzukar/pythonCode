import requests

# Replace with your actual API key
API_KEY = 'EssNh0Nk2zSMUrn31DNbEbTgGXz4is9THTSiSSXwr4epV6zgKMkKJ7W83i5a'

# Define the endpoint URL
url = 'https://api.lix-it.com/v1/search/sales/facet'

# Set up the headers
headers = {
    'Authorization': f'{API_KEY}',
    'Content-Type': 'application/json'
}

# Define the search parameters
params = {
    'type': 'profile',
    'query': 'role:Sales title:Manager region:California'  # example role, title, and region
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the results
    for item in data['results']:
        print(item)
else:
    print(f'Error: {response.status_code}')
    print(response.text)