import requests
import json
import random
from datetime import datetime, timedelta

# Function to generate a random date in yyyy-mm-dd format
def random_birthdate(start_year=1900, end_year=2023):
    # Generate a random date
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    time_delta = end_date - start_date

    random_days = random.randint(0, time_delta.days)
    random_date = start_date + timedelta(days=random_days)

    return random_date.strftime('%Y-%m-%d')

# Generate a random birthdate
birthdate = random_birthdate()

url = "https://thinking-tester-contact-list.herokuapp.com/contacts"

payload = json.dumps({
  "firstName": "John",
  "lastName": "Doe",
  "birthdate": birthdate,
  "email": "jdoe@fake.com",
  "phone": "8005555555",
  "street1": "1 Main St.",
  "street2": "Apartment A",
  "city": "Anytown",
  "stateProvince": "KS",
  "postalCode": "12345",
  "country": "USA"
})

headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzI2MWNlZjAxZjRjMDAwMTM3ZTVhMzAiLCJpYXQiOjE3MzA1NTEwMjN9.jBJeyG-Drrer1lVqoi0Q2KnWG5UwKHvhG6_B-VFhuEk',

  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
