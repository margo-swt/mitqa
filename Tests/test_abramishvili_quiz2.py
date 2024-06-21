import requests
import json

booking_url = "https://automationintesting.online/booking/"


def book_room(data):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(booking_url, headers=headers, data=json.dumps(data))
    return response


def test_valid_booking():
    valid_booking_data = {
        "bookingdates": {
            "checkin": "2024-07-01",
            "checkout": "2024-07-05"
        },
        "email": "john.doe@example.com",
        "firstname": "John",
        "lastname": "Doe",
        "phone": "1234567890",
        "roomid": 1
    }
    response = book_room(valid_booking_data)
    print("Positive Test Case:")
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    assert response.status_code == 201, "Expected status code 201"
    # assert "id" in response.json(), "Expected 'id' key in response"
    assert response.json()["booking"]["firstname"] == "John", "Expected 'John' "


def test_invalid_booking():
    invalid_booking_data = {
        "bookingdates": {
            "checkin": "2024-07-01",
            "checkout": "2024-07-05"
        },
    }
    response = book_room(invalid_booking_data)
    print("Negative Test Case:")
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    assert response.status_code == 400, "Expected status code 400"
    assert "error" in response.json(), "Expected 'error' key"


test_valid_booking()
test_invalid_booking()

print("\nAll tests completed!")