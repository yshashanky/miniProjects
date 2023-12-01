# Second API call with path variables, query parameters, and headers, where the path variables are obtained from the response of the first API call:

import requests

# First API Call
url1 = 'https://api.example.com/endpoint1'
params1 = {
    'param1': 'value1',
    'param2': 'value2'
}
headers1 = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_dummy_token'
}

response1 = requests.get(url1, params=params1, headers=headers1)

if response1.status_code == 200:
    data1 = response1.json()
    # Extract path variables from the response
    variable1 = data1['variable1']
    variable2 = data1['variable2']
else:
    print(f'Request failed with status code: {response1.status_code}')
    exit()

# Second API Call
url2 = f'https://api.example.com/endpoint2/{variable1}/{variable2}'
params2 = {
    'query_param1': 'value1',
    'query_param2': 'value2'
}
headers2 = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_dummy_token'
}

response2 = requests.get(url2, params=params2, headers=headers2)

if response2.status_code == 200:
    data2 = response2.json()
    # Process the response data from the second API call
    print(data2)
else:
    print(f'Request failed with status code: {response2.status_code}')

# In the updated code example, the first API call remains the same. After receiving a successful response (status_code == 200), the path variables (variable1 and variable2) are extracted from the response JSON.
# In the second API call, the URL is constructed using the extracted path variables (url2). Additionally, the params2 dictionary holds the query parameters for the second API call.
# You can update the url2, params2, and headers2 variables as per your specific requirements.
# After making the second API call, you can process the response data (data2) according to your needs.
# Ensure that you replace 'https://api.example.com/endpoint1' and 'https://api.example.com/endpoint2' with the actual API endpoints you are working with. Also, update the headers and path variable extraction logic based on your API's response structure.
