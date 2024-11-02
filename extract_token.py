import requests
import json
import random
import string

url = "https://thinking-tester-contact-list.herokuapp.com/users"


def generate_random_email(domain="fake.com"):
    # Create a random username
    username_length = random.randint(5, 10)  # Random length between 5 and 10
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))

    # Combine username and domain
    email = f"{username}@{domain}"
    return email


# Example usage
random_email = generate_random_email()
print("Random Email:", random_email)

payload = json.dumps({
    "firstName": "Test",
    "lastName": "User",
    "email": random_email,
    "password": "myPassword"
})

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)

# Print the full response for debugging
print("Response:", response.text)

# Check if the response was successful
if response.status_code == 201:
    response_data = response.json()  # Parse the JSON response
    token = response_data.get("token")  # Extract the token
    print("Extracted Token:", token)
else:
    print("Failed to create user:", response.status_code, response.text)




