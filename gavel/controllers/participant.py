from gavel import app
from flask import Response
@app.route('/project/')
def test():
    return Response("It's worked")
