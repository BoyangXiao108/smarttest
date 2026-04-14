import requests


def test_api_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url, timeout=10)

    
    assert response.status_code == 200

    data = response.json()

    
    assert isinstance(data, list)

    
    assert len(data) > 0

    
    assert "userId" in data[0]
    assert "title" in data[0]