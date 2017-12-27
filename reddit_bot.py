import praw
import reddit_bot_config
import os
import time

def reddit_bot_login():
	print "Logging in"
	reddit = praw.Reddit(username = reddit_bot_config.username,
			password = reddit_bot_config.password,
			client_id = reddit_bot_config.client_id,
			client_secret = reddit_bot_config.client_secret,
			user_agent = "TestBot5765 bot for testing")
	print "Logged in!"
	return reddit

def run_reddit_bot(r, replied_to_comments):
    print "Grabbing comments"

    for comment in r.subreddit('test').comments(limit = 10):
            if "Reply" in comment.body and comment.id not in replied_to_comments and comment.author != r.user.me():
                print "Found a comment ID: " + comment.id
                comment.reply("Test Complete")
                comment.upvote()
                print "Upvoted " + comment.id
                print "Comment replied to" + " Comment ID: " + comment.id
                replied_to_comments.append(comment.id)

                with open ("replied_to_comments.txt","append") as f:
                    f.write(comment.id + "\n")

    print"Will search again in 10 seconds"
    time.sleep(10)

def get_saved_comments():
	if not os.path.isfile("replied_to_comments.txt"):
		replied_to_comments = []
	else:
		with open("replied_to_comments.txt", "read") as f:
			replied_to_comments = f.read()
			replied_to_comments = replied_to_comments.split("\n")
			replied_to_comments_ = filter(None, replied_to_comments)
	return replied_to_comments

r = reddit_bot_login()
replied_to_comments = get_saved_comments()
print replied_to_comments

while True:
	run_reddit_bot(r, replied_to_comments)
