things to improve upon:

differentiate between private and does not exist
account for other types of errors (currently account for 32 (could not authenticate) and 34 (account does not exist))
clean up methods more and understand auth
next time, work with json.loads() to make the dict more pythonic. additionally i would be able to
use .get() and see if None is returned if a key does not exist in the dict


TWEET DUPLICATES: what if both users have tweeted the same exact thing?
maybe look at something deeper, like a tweet ID or something, but even then
i added the tweet's text to the tweet list, not a tweet object. hmm...