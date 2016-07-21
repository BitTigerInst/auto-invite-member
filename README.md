This is a tool to add or update membership of an organization. It depends on python library ```requests``` and followed newest [github api](https://developer.github.com/v3/)

# Preparation

We need a csv file containing all names and github usernames we want to add as a certain member.
This example file located in ```/data/member.csv```.
Format like this:

```
foo,bar
foo1,bar1
```

# Python library
We recommend to use virtualenv as developing environment.
We can install all needed libraries like:
```
pip install -r requirements.txt
```

# Run 
We can now run this function:

``` Python
# this fuction use [basic authentication](https://developer.github.com/v3/auth/#basic-authentication) 
username = YOUR_GITHUB_USERNAME
token = YOUR_OWN_TOKEN

# csv path
path = "../data/member.csv"
# your organization name
org = YOUR_ORGANIZATION NAME

# run the function
invite_member(path, org, username, token)
```
