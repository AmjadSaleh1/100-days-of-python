import os
from internetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_SPEED = 150
PROMISED_UP = 12
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = "ENTERPASSWORD"

ist = InternetSpeedTwitterBot()
ist.get_internet_speed()
ist.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)

