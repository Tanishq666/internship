import requests


def short_url(full_link):
    api_key = "215a0a80bbcaff012e8c59173242c70a75a58"
    base_url = "https://cutt.ly/api/api.php"
    links = {'key': api_key, 'short': full_link}
    request = requests.get(base_url, params=links)
    data = request.json()

    print('')

    try:
        short_link = data['url']['shortLink']
        print('Link:', short_link)
    except:
        status = data['url']['status']
        print("Error Status:", status)


link = input("Enter a Link:")

short_url(link)
