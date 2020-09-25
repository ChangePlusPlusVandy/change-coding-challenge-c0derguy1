import requests
from requests_oauthlib import OAuth1
import random


# determining url structure
user_base_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="


def auth_user():

    # declaring auth keys
    client_key = 'hGbwYH2fJ6rDb3lStaQvd55BK'
    client_secret = 'aEwZHkMJ8foOb4sFZkUJKzXWvGQh8Prbuut2VApuQOkOaKhAdj'

    # passing authentication parameters
    url = "https://api.twitter.com/1.1/account/verify_credentials.json"
    auth = OAuth1(client_key, client_secret)
    requests.get(url, auth=auth)

    return auth


def verify_user(username):
    auth = auth_user()
    r = requests.get(user_base_url + username, auth=auth).json()
    for keys in r:

        # does not exist: 'errors'
        if 'errors' in keys and r['errors'][0]['code'] > 0: # more specifically, 32 or 34 (check readme.txt)
            print("are you sure that account exists?")
            return False

        # avoiding json error by checking that this key does not exist before checking its value
        elif 'error' not in r: # just in case
            print("username OK")
            return True

        # private account: 'error' (could also mean that account has been suspended)
        elif r['error'] == 'Not authorized.':
            print("private or suspended acc. please try again")
            return False


def get_tweets(username, num_tweets = 20):
    tweet_url = user_base_url + username + "&count=" + str(num_tweets)

    # declaring tweet list
    user_tweets = []

    # gathering tweets
    r = requests.get(tweet_url, auth=auth_user()).json()
    for tweet in r:
        if tweet['in_reply_to_status_id'] is None and 'retweeted_status' not in tweet:
            user_tweets.append(tweet['text'])
        else:
            continue

    return user_tweets


# game time! let's set the default score
user_score = 0

# keeping track of current round
current_round = 0

while True:
    try:
        rounds = int(input("welcome to the TweetRetriever™! how many rounds would you like to play?\n"))
        break
    except ValueError:
        print("that's not an int!")

# initializing username variables
user_one = ""
user_two = ""

while True:
    user_one = input("enter first twitter username without the @")
    if verify_user(user_one):
        break
    else:
        continue

while True:
    user_two = input("enter second twitter username without the @")
    if user_two == user_one:
        print("whoa there, you can't enter the same username twice!")
        continue
    if verify_user(user_two):
        break
    else:
        continue

user_one_tweets = get_tweets(user_one)
user_two_tweets = get_tweets(user_two)

while current_round < rounds:
    print("you ready for the tweet?")
    game_tweet = random.choice(user_one_tweets + user_two_tweets)
    print(game_tweet)

    # assuming no duplicate tweets
    is_user_one = game_tweet in user_one_tweets
    is_user_two = game_tweet in user_two_tweets

    selection_string = "type 1 for " + user_one + " and 2 for " + user_two + "\n"

    while True:
        try:
            user_selection = int(input(selection_string))
        except ValueError:
            print("that's not an int!")

        if user_selection == 1:
            if is_user_one:
                print("congratulations! you are correct!")
                user_score += 1
            else:
                print("wrong! it was user 2.\n")
            break

        elif user_selection == 2:
            if is_user_two:
                print("congratulations! you are correct!")
                user_score += 1
            else:
                print("wrong! it was user 1.\n")
            break

        elif user_selection != 1 and user_selection != 2:
            print("invalid entry. try again.")

    current_round += 1

print("thanks for playing, partner! your score is", user_score)
