IMPORTANT: uses modules requests, requests_oauthlib (specifically OAuth1), and random

things to improve upon:

- i think i fixed the problem with differentiating between private accounts and accounts that don't exist. see next point:
- learn how to deal with dicts better! next time, work with json.loads() to make the dict more pythonic (although requests has a built in .json() method). additionally i would be able to use .get() and see if None is returned if a key does not exist in the dict. the 'error' key exists when the account is private, but 'errors' instead exists when authentication fails or if the account does not exist...
- i could have done a better job organizing the methods, as i have a few repetitive segments in my code (e.g. with the auth and when concatenating strings to form the request URL(s)). trying to centralize some parts of the code ended up not working too well, probably because i don't fully understand OAuth1 yet.
- account for other types of errors (currently account for 32 (could not authenticate) and 34 (account does not exist) using error > 0)

for example:
- private (or suspended, apparently this message is returned in both situations) account:
{'request': '/1.1/statuses/user_timeline.json', 'error': 'Not authorized.'}

- does not exist:
{'errors': [{'code': 34, 'message': 'Sorry, that page does not exist.'}]}

- could not authenticate (i found that if i put a \ at the beginning of the username, i got this, showing that it probably messed up the URL)
{'errors': [{'code': 32, 'message': 'Could not authenticate you.'}]}

- interestingly enough, when you type a blank space in the username at the beginning, the username is parsed fine (might have to do with python's input function), but when a space is typed in between two words (e.g. kanye west), the account is "suspended or private" according to my program, but the json says i am not authorized to access this account. might be worth looking into this, in case some sneaky user decides to type in a clearly invalid username.

- clean up methods more and understand OAuth1 and authentication in general
- take a look at tweepy and other libraries (maybe BeautifulSoup? not sure if twitter's automatic page updating would come into play there or not) instead of trying to just use requests (i wanted a challenge)
- work on making a GUI with TkInter and figure out how to extract images from a tweet (again, tweepy might be easier for this) and display the images

- (POSSIBLY) HUGE ISSUE: Tweet Duplicates
what if both users have tweeted the same exact thing? in order to simplify things, i put the tweets from both users into one big list, and i don't think there's an easy way to track whether a string came from one list or another. maybe i should look at something deeper, like a tweet ID or something, but even then, in this program i add the tweet's text to the tweet list, not tweet "objects" or entire json dicts to the tweet list. hmm...

- another thing to consider: what if the user has 0 tweets? for example, user @asdfmovie1 has 0 tweets, and somehow the program just prompts the user for another first/second username (which is convenient, but i haven't been able to find a condition under which i can print out a message notifying the user if there aren't any tweets posted by the account), and if you run print(r.json()) you get a blank list [], but i haven't been able to successfully use this fact to my advantage. the program works OK, but i gotta find a workaround for this... what condition could it be?
- also: what if the number of requests exceeds the # of tweets posted? i assume twitter would just stop searching when the max # of tweets has been reached.

overall, i gotta use python more often and learn the language's styling conventions. making this project has been a blast! thank you for the program idea Change++! :D