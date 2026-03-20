import requests


def get_users():
    url = "https://jsonplaceholder.typicode.com/user"
    
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("API failed with status:", response.status_code)
            return []   # safe return

        return response.json()

    except Exception as e:
        print("Error:", e)
        return []


def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("API failed with status:", response.status_code)
            return []

        return response.json()

    except Exception as e:
        print("Error:", e)
        return []