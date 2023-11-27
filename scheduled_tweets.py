 #Automating social media marketing with Twitter APIs
# library twython

"""
Frfeee T
For write-only use cases and testing the X API

    Rate limited access to v2 posting and media upload endpoints 
    1,500 posts per month - posting limit at the app level
    1 app ID
    Login with X 
    Free
"""
"""Automation rules for X
 Ground Rules

Do!
 

    Build solutions that automatically broadcast helpful information in posts.
    Run creative campaigns that auto-reply to users who engage with your content.
    Build solutions that automatically respond to users in Direct Messages.
    Try new things that help people (and comply with our rules).
    Make sure your application provides a good user experience and performs well — and confirm that remains the case over time.
     

Don’t!
 

    Violate these or other policies. Be extra mindful of our rules about abuse and user privacy.
    Abuse the X API or attempt to circumvent rate limits.
    Use non-API-based forms of automation, such as scripting the X website. The use of these techniques may result in the permanent suspension of your account.
    Spam or bother users, or otherwise send them unsolicited messages.
"""


from twython import Twython
import os
"""
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OATH_TOKEN_SECRET = ''

""""""The issue is with your Twitter developer account access level. 
Free Twitter developer accounts only have access to a limited subset of endpoints,
and unfortunately, none of the methods from Twython that involve updating your Twitter status 
fall within that subset. If you need to update your Twitter status using Twython, 
you will need to upgrade your Twitter developer account to a higher access level."""
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OATH_TOKEN_SECRET)
twitter.verify_credentials()
twitter.update_status(status='Hello, here is a practice tweet or Xet?')



print('Tweet Text', tweet['text'])
print('Tweet created at:',tweet['created_at'])
print('Tweeted by:',tweet['entities']['user_mentions'][0]['name'])
print('Retweeted:',tweet['retweet_count'])

#scheduling tweets

from datetime import datetime 
import pytz, time 
from pytz import timezone 
import tweet_config as config 


while True:
    for msg in config.scheduled_messages: 
        print msg["timezone"] 
        tz = timezone(msg["timezone"]) 
        utc = pytz.utc 
        utc_dt = datetime.utcnow().replace(tzinfo=utc) 
        au_dt = utc_dt.astimezone(tz) 
        sday = au_dt.strftime('%Y-%m-%d') 
        stime = au_dt.strftime('%H:%M') 
        print "Current Day:Time", sday, stime 
        if sday == msg["day"]: 
                    if stime == msg["time"]: 
                        print "Time", stime 
                        print "Content", msg["content"] 
                        twitter.update_status(status='%s' %
                        msg["content"] ) 
 
 
            print "Running.. Will try in another min" 
            time.sleep(60) 
            tweet_config.py
        offers_sydney = { 
            "content":"Weekend Offers, avail 30% discount today!", 
            "day":"2016-08-27", 






#An introduction to Webhooks

#Implementing Webhooks