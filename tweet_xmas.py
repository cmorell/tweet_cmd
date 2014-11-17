#!/usr/bin/python
import tweepy
import config as twitter_values
import sys, getopt

user=""
text=""
myopts, args = getopt.getopt(sys.argv[1:],"u:m:")


for o, a in myopts:
    if o == '-u':
        user=a
    elif o == '-m':
        text=a
    else:
        print("Usage tweet xmas: %s -u user_name -m message_to_user" % sys.argv[0])
 
# Display input and output file name passed as the args
print ("u : %s and m: %s" % (user,text) )


message = "@"+user + " "+text
#En esta parte nos identifica para poder realizar operaciones
auth = tweepy.OAuthHandler(twitter_values.CONSUMER_KEY, twitter_values.CONSUMER_SECRET)
auth.set_access_token(twitter_values.ACCESS_KEY, twitter_values.ACCESS_SECRET)
 
#update_status('mensaje' o variable) es para actualizar nuestro estado
x = tweepy.API(auth)
x.update_status(message)