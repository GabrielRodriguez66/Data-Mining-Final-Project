from src.TwitterClient import TwitterClient

# creating object of TwitterClient Class
api = TwitterClient()

# query parameters
search_words = "Tati James Charles -filter:retweets"
since = "2019-05-10"

# calling function to get tweets
api.get_tweets(query=search_words, date_since=since, count=2000)

# calculating sentiment stats
api.get_stats()
api.to_csv(r"C:\\Users\Gabriel\Desktop\Data_Mining_Project\results\tweets5.csv")
