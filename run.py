from app import app

# debug = app.config.app_config.debug
debug = True
app.run(host='127.0.0.1', port=8000, debug=debug)
