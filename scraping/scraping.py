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
from PIL import Image
from resizeimage import resizeimage


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


# Takes a myURL string for use for downloading an image, battle identifier string, and
# image number for creation of the newly downloaded file
# Note: image1.jpg will ALWAYS be the original post (for comparison purposes)
def downloadImages(myURL, battleID):

    gotIt = False
    imageNum = 1
    downloadedImageName = 'img' + str(imageNum) + '.jpg'

    try:
        req = requests.get(myURL)
        gotIt = True
    except:
        gotIt = False

    if(gotIt):
        os.chdir("..")
        os.chdir("app/static")

        #NOT IMPLEMENTED:  if the folder doesn't already exist, create it. Otherwise 
        #currently do nothing but return a folder exists error?  dynamic so doesn't reload?
        if not os.path.exists(battleID):
            os.mkdir(battleID)
            os.chdir(battleID)
        else:
            os.chdir(battleID)
        
        while os.path.isfile(downloadedImageName):
            imageNum += 1
            downloadedImageName = 'img' + str(imageNum) + '.jpg'

            if(imageNum > 1000):
                print("Overflowing past what is reasonable - something went wrong!")
                break

        f = open(downloadedImageName, 'wb')
        f.write(req.content)
        f.close()
        with open(downloadedImageName, 'r+b') as f:
            with Image.open(f) as image:
                square = resizeimage.resize_crop(image, [200,200])
                square.save('img' + str(imageNum) + '.sqr.jpg', image.format)
        #resizeImage(downloadedImageName)

        os.chdir("..")
        os.chdir("..")
        
    #else:
        #print("Error getting the image")


# Resize Image - needs modification

#def resizeImage(imageName):
    
 

def main():

    authentication()

    global myReddit
    global PSbattles

    myReddit = praw.Reddit(client_id = config.CLIENT_ID,
        client_secret = config.CLIENT_SECRET,
        user_agent = 'linux:HackED-One-Stop-Photoshop:v0.1 (by u/HackED-Photoshop-Bot)')
    PSbattles = myReddit.subreddit('photoshopbattles')

    URL = []
    top_comments = []
    ID = []
    ratio = []

    URL, ID, ratio, top_comments = getLinks()
    print(ratio)
    arrayCount = -1
    for array in top_comments:
        arrayCount = arrayCount + 1
        downloadImages(URL[arrayCount], ID[arrayCount])
        for str in array:
            downloadImages(str, ID[arrayCount])

    # example:
    # downloadImages('https://i.imgur.com/rVbC2Di.jpg', 'TEST', 6)


def getLinks():
    URL = []
    top_comments = []
    ID = []
    ratio = []
    for submission in PSbattles.top(limit = config.POSTS_TO_LOAD):
        ratio.append(submission.upvote_ratio)
        ID.append(submission.id)
        URL.append(submission.url)
        submission.comments.replace_more(limit=0)
        top_comments.append(list(submission.comments))
    arrayCount = -1
    for array in top_comments:
        arrayCount += 1
        strCount = 0
        for str in array:
            str = str.body
            if "https://i.imgur" and ".jpg" not in str:
                try:
                    array.remove(str)
                except ValueError:
                    pass
            else:
                start = str.find("https://i.imgur")
                end = str.find(".jpg")
                str = str[start:end + 4]
                top_comments[arrayCount][strCount] = str
            strCount += 1
    return(URL, ID, ratio, top_comments)


if __name__ == "__main__":
    main()

# WORKING!  Pulls the top hot titles from the learn python subreddit and prints
# to the console
#for submission in myReddit.subreddit('learnpython').hot(limit=10):
#   print(submission.title)