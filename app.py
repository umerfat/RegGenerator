from flask import Flask
from flask_bootstrap import Bootstrap

# Create our flask application
app = Flask(__name__)
Bootstrap(app)
# Make WSGI interface available at the top
wsgi_app = app.wsgi_app

# We import routes here from routes.py file
from routes import *
# @app.route('/')
# def hello():
#     return """ <!DOCTYPE html>
# <html lang="en">
#     <head>
#         <meta charset="utf-8" />
#         <title>Flask</title>
#     </head>
#     <body>
#         <div> <h2>Welcome to flask</h2> </div>
#     </body>
# </html>
#     """
# Launching our server

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.debug = True
    app.run(HOST, PORT)


