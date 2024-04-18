import requests
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_json():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Check if the status code is 200
    if response.status_code == 200:
        logger.info("GET Success")
        return {
            "status": 200,
            "message": "BTU Success",
            "data": response.json()
        }
    else:
        logger.error("Error: Unexpected status code")
        return {
            "status": response.status_code,
            "message": "Error: Unexpected status code",
            "data": None
        }

def create_data(data):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.post(url, json=data)

    if response.status_code == 201:
        return {
            "status": 201,
            "message": "POST Success",
            "data": response.json()
        }
    else:
        return {
            "status": response.status_code,
            "message": "Error: Unexpected status code",
            "data": None
        }


if __name__ == "__main__":
    result = get_json()
    logger.info(result)

    post_data = {"title": "New Post", "body": "This is a new post"}
    post_result = create_data(post_data)
    logger.info("\nPOST Request Result:")
    logger.info(post_result)