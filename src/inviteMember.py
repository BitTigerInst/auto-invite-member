import requests
import pandas as pd


def invite_member(path, username, token):
    # import data
    df = pd.read_csv(path, names=["name", "github"]).dropna(axis=0, how='all')
    df['state'] = "NaN"

    for i in range(len(df.index)):
        gh = str(df.iloc[i]['github'])
        gh = gh.strip()  # trim spaces
        gh = gh.replace('https://github.com/', '')
        gh = gh.replace('github.com/', '')
        if gh != "nan":
            try:
                print(gh, _invite_member(gh, username, token))
            except Exception:
                pass


def _invite_member(usr, username, token):
    url = "https://api.github.com/orgs/BitTigerInst/memberships/{0}".format(usr)
    data = '{"role":"member"}'
    auth = (username, token)

    r = requests.put(url, data=data, auth=auth)

    return r.json()['state']



