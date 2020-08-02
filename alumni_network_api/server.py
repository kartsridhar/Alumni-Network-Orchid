from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from login import login_route
from signup import signup_route
from verification import verification_route
from selectcategory import select_category_route
from createpost import create_post_route
from deletepost import delete_post_route
from bookmarkpost import addbookmark_post_route,removebookmark_post_route
from getpost import get_post_route
from getuser import get_user_route
from discover import get_category_route
from profile import profile_route
from messages import messages_route

app = Flask(__name__)
CORS(app)
jwt = JWTManager(app)

app.register_blueprint(login_route)
app.register_blueprint(signup_route)
app.register_blueprint(verification_route)
app.register_blueprint(select_category_route)

app.register_blueprint(create_post_route)
app.register_blueprint(delete_post_route)
app.register_blueprint(get_post_route)
app.register_blueprint(addbookmark_post_route)
app.register_blueprint(removebookmark_post_route)
app.register_blueprint(get_user_route)
app.register_blueprint(get_category_route)
app.register_blueprint(profile_route)
app.register_blueprint(messages_route)

if __name__ == "__main__":
	app.config.update(
    SESSION_COOKIE_HTTPONLY=False,
    SECRET_KEY='speakfriend'
    )
	app.run(debug=True,ssl_context=('cert.pem', 'key.pem'))
