import tweepy
import time

#We need Twitter developer account
#after getting the developer account access we deploy one app
#that app will generate the following keys
#Remember, We need read write permission for all the keys
CONSUMER_KEY=''
CONSUMER_SECRET=''
ACCESS_KEY='-'
ACCESS_SECRET=''

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)

FILE_NAME='lastSeenId.txt'

def getLastSeenIds(fileName):
    fRead=open(fileName,'r')
    lastSeenId=int(fRead.read().strip())
    fRead.close()
    return lastSeenId

def storeLastSeenId(lastSeenId,fileName):
    fWrite=open(fileName,'w')
    fWrite.write(str(lastSeenId))
    fWrite.close()
    return
def getHashTag(textList):
    for word in textList:
        if('#' in word):
            import pdb
            pdb.set_trace()
            return word
    
def resposeToTweets():
    lastSeenIds=getLastSeenIds(FILE_NAME)

    mentions=api.mentions_timeline(lastSeenIds,tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        lastSeenId=mention.id
        storeLastSeenId(lastSeenId,FILE_NAME)
        if('#' in mention.full_text):
            textList=mention.full_text.split(' ')
            hashTag=getHashTag(textList)
            import pdb
            pdb.set_trace()
            if('#' in hashTag):
                print('found HashTag',flush=True)
                print('responding back ....',flush=True)
                api.update_status('@'+mention.user.screen_name+' '+hashTag+' '+
                                  'back to you !!',mention.id)
    
while True:
    resposeToTweets()
    time.sleep(15)
    
