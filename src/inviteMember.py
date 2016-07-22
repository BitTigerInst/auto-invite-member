import requests
import pandas as pd


def invite_member(path, org, username, token):
    # import data
    df = pd.read_csv(path, names=["name", "github"]).dropna(axis=0, how='all')
    df['state'] = "NaN"
    index = 0
    index_bad = 0
    for i in range(len(df.index)):
        gh = str(df.iloc[i]['github'])
        gh = gh.strip()  # trim spaces
        gh = gh.replace('https://github.com/', '')
        gh = gh.replace('github.com/', '')
        if gh != "nan":
            try:
                res = _invite_member(gh, org, username, token)
                if res != "active":
                    print(gh, res)
                    index += 1
            except Exception:
                print(gh, "bad username")
                index_bad += 1
    print("active: {0}".format(len(df.index) - index - index_bad))
    print("pending: {0}; not success: {1}".format (index, index_bad))


def _invite_member(usr, org, username, token):
    url = "https://api.github.com/orgs/{0}/memberships/{1}".format(org, usr)
    data = '{"role":"member"}'
    auth = (username, token)

    r = requests.put(url, data=data, auth=auth)

    return r.json()['state']



