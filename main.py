import gspread
from twitter import *

consumer_key = '*'
consumer_secret = '*'
token = '*'
token_secret = '*'

gc = gspread.service_account('credentials.json')
t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# Open a sheet from spreadsheet
wks = gc.open("bot_tweets").sheet1

next_tweet = wks.acell('A2').value

# Post tweet through Twitter API
t.statuses.update(
    status=next_tweet)

# Delete row on success
wks.delete_rows(2)
