from app import app
from datetime import timedelta
import asyncio
import feedparser
import requests
import tweepy


scheduler = app.config.app_config.SCHEDULER
redis = app.config.app_config.REDIS


class TweetRssFeed(object):

    consumer_key = ''
    consumer_secret = ''
    access_key = ''
    access_secret = ''
    auth = tweepy.OAuthHandler(
        consumer_key,
        consumer_secret
    )
    auth.set_access_token(access_key, access_secret)
    twitter_api = tweepy.API(auth)

    @classmethod
    def run_jobs(cls):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cls.tweet_feeds())

    @classmethod
    async def get_feeds(cls):
        feeds = await redis.smembers("feeds")
        return feeds

    @classmethod
    async def tweet_feeds(cls):
        feeds = await cls.get_feeds()
        responses = cls.get_feed_responses(feeds)
        for response in responses:
            cls.tweet_feed(response)

    @classmethod
    def get_feed_responses(cls, feeds):
        responses = []
        for feed in feeds:
            responses.append(
                requests.get(feed)
            )
        return responses

    @classmethod
    def tweet_feed(cls, feed_response):
        feed = feedparser.parse(feed_response.content)
        unique_entries = {
            entry.link: entry
            for entry in feed.entries
        } 
        for entry in unique_entries.values():
            cls.twitter_api.update_status(entry.link)


def run_scheduler():
    job = TweetRssFeed.run_jobs
    cron_string = "5 18 * * *"
    scheduler.cron(
        cron_string,
        job
    )

