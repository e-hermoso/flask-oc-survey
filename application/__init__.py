'''
The __init__.py file is the default file for initialization; similar to index.js file in React or Vue.
Here we move the app object into this file. The application needs to know where it starts by looking into
the main.py file thats because we defined our enviounrment to look into the main.py file. In our main.py file
we import and load the app object.
'''
from flask import Flask
# Special variable (__name__) to identify the current application or module that is being rendered or passed to flask
app = Flask(__name__)

from application import routes
