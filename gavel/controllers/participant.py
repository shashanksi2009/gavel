from gavel import app
from flask import Response
@app.route('/admin/test1')
def test():
    return Response("It's worked")
