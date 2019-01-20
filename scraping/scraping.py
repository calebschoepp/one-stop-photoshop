# Code copied from the quick example guide:
# Using our bot:
    # Your username is: HackED-Photoshop-Bot
    # Your password is: 1234567890
    # Your app's client ID is: VDX4PVjK4BSxKA
    # Your app's client secret is: q5OrTpB4fzg_sGrxccP2yIAho4Y

# Request a token:
# Notice that for acquiring a token, requests are made to https://www.reddit.com


import config
import os
import praw
import requests
import requests.auth

def authentication():

    client_auth = requests.auth.HTTPBasicAuth(config.CLIENT_ID, config.CLIENT_SECRET)
    post_data = {"grant_type": "password", "username": config.REDDIT_USERNAME, "password": config.REDDIT_PASSWORD}
    headers = {"User-Agent": "linux:HackED-One-Stop-Photoshop:v0.1 (by u/HackED-Photoshop-Bot)"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    response.json()
    {u'access_token': u'fhTdafZI-0ClEzzYORfBSCR7x3M',
     u'expires_in': 3600,
     u'scope': u'*',
     u'token_type': u'bearer'}

    # Use the token:
    # Notice that for using the token, requests are made to https://oauth.reddit.com
    headers = {"Authorization": "bearer fhTdafZI-0ClEzzYORfBSCR7x3M", "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
    response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
    response.json()
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
     u'name': u'HackED-Photoshop-Bot',
     u'over_18': True}


# Takes a myURL string for use for downloading an image, battle number integer, and
# image number for creation of the newly downloaded file
def downloadImages(myURL, battleNum, imageNum):

    req = requests.get(myURL)
    downloadedImageName = str(battleNum) + '.' + str(imageNum) + '.jpg'
    
    os.chdir("..")
    os.chdir("app/static")

    f = open(downloadedImageName, 'wb')
    f.write(req.content)
    f.close()
 

def main():

    authentication()

    global myReddit
    global PSbattles

    myReddit = praw.Reddit(client_id = config.CLIENT_ID,
        client_secret = config.CLIENT_SECRET,
        user_agent = 'linux:HackED-One-Stop-Photoshop:v0.1 (by u/HackED-Photoshop-Bot)')
    PSbattles = myReddit.subreddit('photoshopbattles')
    URL = []
    
    # for submission in PSbattles.top(limit = config.POSTS_TO_LOAD):
    #     URL.append(submission.url)
    #     top_comments = list(submission.comments)
    # for j in range(0, config.POSTS_TO_LOAD):
    #     print(str(top_comments[j].body))
    #     print(' ')


    # test:

    downloadImages('https://i.imgur.com/rVbC2Di.jpg', 0, 0)




if __name__ == "__main__":
    main()

# WORKING!  Pulls the top hot titles from the learn python subreddit and prints
# to the console
#for submission in myReddit.subreddit('learnpython').hot(limit=10):
#   print(submission.title)