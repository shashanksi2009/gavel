from gavel import app
from flask import Response , render_template
@app.route('/project/')
def submitProject():
    return render_template("projectForm.html")
