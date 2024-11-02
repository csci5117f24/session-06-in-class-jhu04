from flask import Flask, render_template, request, redirect, url_for, session
import db
import os
import psycopg2
from urllib.parse import urlencode, quote_plus
from functools import wraps

from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]
# db.setup()

# oauth = OAuth(app)

# oauth.register(
#     "auth0",
#     client_id=os.environ.get("AUTH0_CLIENT_ID"),
#     client_secret=os.environ.get("AUTH0_CLIENT_SECRET"),
#     client_kwargs={
#         "scope": "openid profile email",
#     },
#     server_metadata_url=f'https://{os.environ.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
# )


# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         if 'user' not in session:
#             # Redirect to Login page here
#             return redirect('/')
#         return f(*args, **kwargs)  # do the normal behavior -- return as it does.

#     return decorated

# @app.route("/login")
# def login():
#     # TODO: why should I enable _external?
#     return oauth.auth0.authorize_redirect(
#         redirect_uri=url_for("callback", _external=True)
#     )


# # TODO: why POST?
# @app.route("/callback")
# def callback():
#     session["user"] = oauth.auth0.authorize_access_token()
#     return redirect("/")


# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(
#         "https://"
#         + os.environ.get("AUTH0_DOMAIN")
#         + "/v2/logout?"
#         + urlencode(
#             {
#                 "returnTo": url_for("hello", _external=True),
#                 "client_id": os.environ.get("AUTH0_CLIENT_ID"),
#             },
#             quote_via=quote_plus
#         )
#     )


# @app.route("/secret")
# @requires_auth
# def secret():
#     return "<p>secret</p>"


# @app.route('/')
# @app.route('/<name>')
# def hello(name=None):
#     print(session)
#     return render_template("hello.html", name=session.get("user", "Guest"))
#     # with psycopg2.connect(os.environ['DATABASE_URL']) as conn:
#     #     with conn.cursor() as cur:
#     #         cur.execute("select * from tmp")
#     #         return render_template('hello.html', name=cur.fetchone()[0])


# @app.route('/8')
# def eight():
#     return f"<p>{db.get_color('white')}</p>"


# @app.route("/new_color", methods=["POST"])
# def new_color():
#     color_code = request.form.get("color")
#     name = request.form.get("name")
#     db.create_color(color_code, name)
#     return redirect(url_for("hello"))

# @app.route("/upload_image")
# def upload_image():
#     pass

@app.route('/')
def hello():
    print(request.args)
    return f"{request.args}", 200
