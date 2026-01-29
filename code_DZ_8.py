import requests

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = response.json()
    for i in range(5):
        print("Пост", i + 1)
        print("Заголовок:", posts[i]['title'])
        print("Тело:", posts[i]['body'])
        print("-" * 40)

fetch_posts()