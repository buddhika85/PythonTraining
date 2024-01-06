class TwitterUser:
    def __init__(self, username, followers_count, tweets):
        self.username = username
        self.followers_count = followers_count
        self.tweets = tweets
    def post_tweet(self, content):
        self.tweets += 1
        return f"{self.username} posted a new tweet: '{content}'"
    def add_followers(self, count):
        self.followers_count += count
    def __str__(self):
        return f"{self.username} has {self.followers_count} followers and made {self.tweets} tweets"

user = TwitterUser("elon_musk", 500, 20)
user.add_followers(15)
print(user.post_tweet("I'm renaming this platform to X!"))

print(user.followers_count)
print(user.tweets)