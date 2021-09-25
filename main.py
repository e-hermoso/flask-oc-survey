"""
In this sample, the Flask app object is contained within the application *module*;
that is, application contains an __init__.py along with relative imports. Becasue
of this structure, a file like main.py cannot be run directly as the startup file
through Gunicorn; the resul is "Attempted relative import in non-package."

The solution is to provide a simple alternate startup file, like this present
main.py, that just imports the app object. You can then just specify
main:app in the Gunicorn command.
"""

"""
Importing app variable from application/__init__.py
When importing from application directory it will look for
__init__.py file by default.
"""
from application import app
