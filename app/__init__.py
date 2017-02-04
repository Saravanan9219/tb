from sanic import Sanic


app =  Sanic(__name__)


__all__ = ['app']


from config import AppConfiguration
app.config.app_config = AppConfiguration(app)


from app.rss import rss_bp
app.blueprint(rss_bp)
