import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("search", type=str)
args = parser.parse_args()

url = f"https://api.github.com/users/{args.search}/events"
response = requests.get(url)

if response.status_code == 200:
    events = response.json()
    for event in events:
        print(f"{event['type']} at {event['repo']['name']} on {event['created_at']}")
else:
    print("Error:", response.status_code, response.text)