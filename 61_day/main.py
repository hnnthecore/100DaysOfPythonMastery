# -----------------------------------------------
# 1. IMPORTING FLASK
# -----------------------------------------------
# Flask is a lightweight web framework.
# It allows us to create a web server using Python.

from flask import Flask


# -----------------------------------------------
# 2. CREATING THE FLASK APP
# -----------------------------------------------
# Flask needs to know where it is being run from.
# __name__ is a special built-in variable in Python.
#
# If this file is run directly:
#   __name__ == "__main__"
#
# If this file is imported somewhere else:
#   __name__ == "main" (or filename)
#
# Flask uses this information to:
# - locate templates
# - locate static files
# - understand project structure

app = Flask(__name__)


# -----------------------------------------------
# 3. WHAT IS A DECORATOR?
# -----------------------------------------------
# A decorator is a function that wraps another function.
# It modifies or enhances the behavior of that function.
#
# Flask uses decorators to:
# - associate a URL with a Python function
#
# @app.route("/") means:
# "When someone visits '/', run the function below"


@app.route("/")
def home():
    """
    This function runs when a user visits:
    http://127.0.0.1:5000/

    Flask automatically:
    - receives the HTTP request
    - calls this function
    - sends the return value back as an HTTP response
    """
    return "Welcome to Flask! This is the home page."


# -----------------------------------------------
# 4. MULTIPLE ROUTES = MULTIPLE FUNCTIONS
# -----------------------------------------------
# Each route is just a Python function.
# URLs are mapped to functions using decorators.


@app.route("/about")
def about():
    """
    This function runs when a user visits:
    http://127.0.0.1:5000/about
    """
    return "This page explains what this Flask app is about."


@app.route("/contact")
def contact():
    """
    Another route.
    Notice how simple routing is:
    URL ➜ Python function ➜ Response
    """
    return "Contact us at: hello@example.com"


# -----------------------------------------------
# 5. FUNCTIONS AS FIRST-CLASS OBJECTS
# -----------------------------------------------
# In Python, functions can be:
# - passed as arguments
# - returned from other functions
#
# Flask decorators work because of this feature.


def simple_decorator(func):
    """
    A very basic custom decorator to demonstrate the concept.
    """

    def wrapper():
        return f"[Decorator Added] {func()}"

    return wrapper


@simple_decorator
def demo_function():
    """
    This function is wrapped by simple_decorator.
    The decorator modifies what this function returns.
    """
    return "This function was decorated"


# -----------------------------------------------
# 6. RUNNING THE FLASK SERVER
# -----------------------------------------------
# This block ensures that:
# - the server runs ONLY when this file is executed directly
# - the server does NOT auto-run if this file is imported

if __name__ == "__main__":
    # app.run() starts Flask’s built-in development server
    #
    # debug=True:
    # - auto reloads the server on code changes
    # - shows helpful error messages
    #
    # This is ONLY for development, not production

    app.run(debug=True)
