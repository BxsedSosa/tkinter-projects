import requests, json

curr = "EUR"
url = f"https://v6.exchangerate-api.com/v6/bec77be4071bc0862bff85eb/latest/{curr}"

response = requests.get(url)
pretty_print = json.dumps(response.json(), indent=4)

print(pretty_print)
