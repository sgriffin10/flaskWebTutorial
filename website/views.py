from flask import Blueprint,render_template
'''
defines url endpoints for front end of site
define that this file is a blueprint for our app
don't need to define all routes in one file
'''

views = Blueprint('views',__name__)

@views.route('/') #decorator
def home(): #route
    return render_template("home.html")
    # return "<h1>Test</h1>"