from app.rss import rss_bp
from app.rss.utils import add_feed
from sanic.views import HTTPMethodView
from sanic.response import text, json


class RssView(HTTPMethodView):
    
    async def post(self, request):
        data = request.json.get("feed_url")
        await add_feed(data)
        return json({"detail": "ok"})
    
    def get(self, request):
        return text("Hello World! \r\n")


rss_bp.add_route(RssView.as_view(), '/')
