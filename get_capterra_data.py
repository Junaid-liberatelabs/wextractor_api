import requests
def get_capterra_data(id,wex_token,page_no=0):
    """
    Fetches reviews from Glassdoor via the Wextractor API.
    """
    url = "https://wextractor.com/api/v1/reviews/capterra"
    params = {
        "id": id,

        "auth_token": wex_token,
        "offset": page_no,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        reviews = data.get("reviews", [])
        return reviews
    else:
        print(f"Failed to fetch reviews. Status Code: {response.status_code}")
        print(response.text)
        return []
