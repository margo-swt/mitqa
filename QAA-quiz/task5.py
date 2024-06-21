import requests
import json

url = "https://automationintesting.online/message/"

def send_message(data):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response

def test_empty_submission():
    empty_data = {}
    response = send_message(empty_data)
    print("Empty Submission Response:")
    print("Status Code:", response.status_code)
  #  print("Response Body:", response.json())
    
    assert response.status_code == 400, "Expected status code 400"
    assert "error" in response.json(), "Expected 'error' key in response"

def test_correct_data_submission():
    correct_data = {
        "messageid": 15,
        "name": "Alex",
        "email": "alex@example.com",
        "phone": "12345678905555",
        "subject": "something",
        "description": "This is a test message",
        "messages": [
            {
                "id": 2,
                "name": "Alex",
                "subject": "something",
                "read": False
            }
        ]
    }
    response = send_message(correct_data)
    print("\nCorrect Data Submission Response:")
    print("Status Code:", response.status_code)
    # print("Response Body:", response.json())
    
    assert response.status_code == 201, "Expected status code 201"
    assert "messageid" in response.json(), "Expected 'messageid' key"
    assert response.json()["name"] == "Alex", "Expected name 'Alex'"
    assert response.json()["description"] == "This is a test message"


test_empty_submission()
test_correct_data_submission()

print("\nAll tests completed!")
