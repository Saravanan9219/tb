from app import app 


redis = app.config.app_config.REDIS


async def add_feed(feed_url: str):
    await redis.sadd('feeds', feed_url)
