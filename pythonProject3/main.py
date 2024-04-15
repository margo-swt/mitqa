import requests

# Define the base URL of the REST API
BASE_URL = "https://jsonplaceholder.typicode.com"


# Function to get all posts
def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        return response.json()
    else:
        return None


# Function to get a specific post by its ID
def get_post_by_id(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None


# Function to create a new post
def create_post(title, body, user_id):
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(f"{BASE_URL}/posts", json=data)
    if response.status_code == 201:
        return response.json()
    else:
        return None


# Function to update an existing post
def update_post(post_id, title, body):
    data = {
        "title": title,
        "body": body
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# Function to delete a post
def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        return True
    else:
        return False


# Example usage
if __name__ == "__main__":
    # Get all posts
    print("All Posts:")
    print(get_posts())

    # Get post by ID
    print("\nPost with ID 1:")
    print(get_post_by_id(1))

    # Create a new post
    new_post = create_post("New Title", "New Body", 1)
    print("\nNewly Created Post:")
    print(new_post)

    # Update an existing post
    updated_post = update_post(1, "Updated Title", "Updated Body")
    print("\nUpdated Post:")
    print(updated_post)

    # Delete a post
    print("\nDeleting Post with ID 1:")
    print(delete_post(1))
