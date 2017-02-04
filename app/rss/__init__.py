from sanic import Blueprint


rss_bp = Blueprint('rss', url_prefix='rss')


from app.rss import scheduler
scheduler.run_scheduler()


from app.rss import views  # always should be at the end
