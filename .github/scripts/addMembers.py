import json
import pandas as pd
import requests
import datetime as dt
import os

api = "https://api.github.com/"
token = os.environ['GITHUB_TOKEN']

def main():
    with open('results.json', 'r') as file:
        data = json.load(file)
        usernames = data["Github Username"]
        timestamp = data["Timestamp"]
        days = []
        for val in timestamp:
            days.append(val.split()[0])
        today = dt.date.today()-dt.timedelta(days=1)
        d1 = today.strftime("%m/%d/%Y")
        new_users = [usernames[i] for i in range(len(days)) if days[i]==d1]
        for user in new_users:
            endpoint = f"orgs/VICTOR-Community/teams/victoraccess/membership/{user}"
            url = f"{api}{endpoint}"
            response = requests.put(url, auth=("volcanocyber",token))
            print(response.json())
        
if __name__ == "__main__":
    main()