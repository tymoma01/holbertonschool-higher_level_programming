import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: " + str(response.status_code))
    
    if response.status_code == 200:
        res = response.json()

        for elt in res:

            print(elt['title'])
    else:
        print("Failed to fetch posts:", response.status_code)


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: " + str(response.status_code))
    
    if response.status_code == 200:
        res = response.json()
        data = [
                    {
                        "id": post["id"], 
                        "title": post["title"], 
                        "body": post["body"]
                    } 
                    for post in res
                ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
    else:
        print("Failed to fetch posts:", response.status_code)