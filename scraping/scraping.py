# Code copied from the quick example guide:
# Assuming:
    # Your username is: reddit_bot
    # Your password is: snoo
    # Your app's client ID is: p-jcoLKBynTLew
    # Your app's client secret is: gko_LXELoV07ZBNUXrvWZfzE3aI

# REPLACING IN PROGRESS

# Request a token:
# Notice that for acquiring a token, requests are made to https://www.reddit.com
In [1]: import requests
In [2]: import requests.auth
In [3]: client_auth = requests.auth.HTTPBasicAuth('p-jcoLKBynTLew', 'gko_LXELoV07ZBNUXrvWZfzE3aI')
In [4]: post_data = {"grant_type": "password", "username": "reddit_bot", "password": "snoo"}
In [5]: headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
In [6]: response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
In [7]: response.json()
Out[7]: 
{u'access_token': u'fhTdafZI-0ClEzzYORfBSCR7x3M',
 u'expires_in': 3600,
 u'scope': u'*',
 u'token_type': u'bearer'}

# Use the token:
# Notice that for using the token, requests are made to https://oauth.reddit.com
In [8]: headers = {"Authorization": "bearer fhTdafZI-0ClEzzYORfBSCR7x3M", "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
In [9]: response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
In [10]: response.json()
Out[10]: 
{u'comment_karma': 0,
 u'created': 1389649907.0,
 u'created_utc': 1389649907.0,
 u'has_mail': False,
 u'has_mod_mail': False,
 u'has_verified_email': None,
 u'id': u'1',
 u'is_gold': False,
 u'is_mod': True,
 u'link_karma': 1,
 u'name': u'reddit_bot',
 u'over_18': True}