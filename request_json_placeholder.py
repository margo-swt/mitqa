import requests
import json

url = "https://thinking-tester-contact-list.herokuapp.com/contacts"

payload = json.dumps({
  "firstName": "John",
  "lastName": "Doe",
  "birthdate": "1970-01-01",
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
