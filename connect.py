import tweepy

consumer_token = "oBsmOC58LUwperuA6Tg8M5HRB"
consumer_secret = "D8VhsiqvDXKElv7sJjP6ORlKKH4DWdppVZpCrAdE75Ffw0aSwh"
access_token = "1371060001754714116-XwzthDYHiQknjwItgtLugDbROdlU5u"
access_token_secret = "abck6Y4zt9aLWawWyYLhQKANJZAnsLMxG67iCsTbSMm8r"


auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print("Error! Failed to get request token.")

print(redirect_url)

verifier = input('Verifier:')

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print("Error! Failed to get access token.")

new_token = auth.access_token
new_secret = auth.access_token_secret

print("access_token" + new_token)
print("access_token_secret" + new_secret)
