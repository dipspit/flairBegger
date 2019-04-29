#!/usr/bin/env python    

import praw

reddit = praw.Reddit(client_id=' <id> ', client_secret=' <secret> ', password=' <password> ', user_agent='flairBegger by /u/_bama', username=' <username> ')

sub = 'vzwemployees'

# get the users who are already flaired
flaired_users = [flair['user'].name for flair in reddit.subreddit(sub).flair(limit=None)]

# get the list of contributors
contributors = [user.name for user in reddit.subreddit(sub).contributor(limit=None)]

# remove already flaired users from the mailing list
create_list = list(set(contributors) - set(flaired_users))

# for every user in the mailing list send a modmail message
for user in create_list:
    reddit.redditor(user).message('<subject>', "<custom message that can include markdown>", from_subreddit='<the subreddit>')