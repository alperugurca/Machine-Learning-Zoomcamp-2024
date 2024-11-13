import requests
import json

# Test data
test_data = {
    'Hours per day': 3.0,
    'Anxiety': 7.0,
    'Depression': 5.0,
    'Insomnia': 6.0,
    'OCD': 4.0,
    'Fav genre': 'Rock'
}

# Make prediction request
response = requests.post('http://localhost:5000/predict', 
                        json=test_data)

# Print results
print(response.json())