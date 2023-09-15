import gspread
import pandas as pd
import requests
import datetime as dt
import os

api = "https://api.github.com/"
token = os.environ['GITHUB_TOKEN']

def main():
    gc = gspread.service_account()
    sh = gc.open("VICTOR Registration (Responses)")
    vals = pd.DataFrame(sh.get_worksheet(0).get_all_records())
    usernames = vals["What is your GitHub username?"].values
    timestamp = vals["Timestamp"].values
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