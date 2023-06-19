from flask import Flask, jsonify, redirect, request, render_template
import json
import hashlib
import os
import authModel
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from dotenv import load_dotenv
datas = load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Bakeli API"
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route("/")
def home():
    print("Data: ", os.environ.get("DBNAME"))
    return "Hello World {}".format(os.environ.get("DBUSER"))


@app.route("/register", methods=["POST", "DELETE", "GET"])
def client():
    if request.method == 'POST':

        # verify the token
        # TO do after we create first credentials

        # get the client_id and secret from the client application
        client_id = request.form.get(
            "client_id", request.json["client_id"])
        client_secret_input = request.form.get(
            "client_secret", request.json["client_secret"])
        is_admin = request.form.get(
            "is_admin", request.json["is_admin"])

        if is_admin:
            is_admin = True
        else:
            is_admin = False

        # the client secret in the database is "hashed" with a one-way hash
        hash_object = hashlib.sha1(
            bytes(client_secret_input, encoding="utf-8"))
        hashed_client_secret = hash_object.hexdigest()
        print("Data: {} et {}".format(client_id, is_admin))
        # make a call to the model to authenticate
        createResponse = authModel.create(
            client_id, hashed_client_secret, is_admin)

        return jsonify({'New User Created': createResponse})

    elif request.method == 'DELETE':
        # not yet implemented
        return jsonify({'New User Deleted': False})
    else:
        return render_template("register.html", name="register")


@app.route("/auth", methods=["POST", "GET"])
def auth():
    # get the client_id and secret from the client application

    if request.method == "POST":
        client_id = request.form.get(
            "client_id", request.json["client_id"])
        client_secret_input = request.form.get(
            "client_secret", request.json["client_secret"])

        '''if client_id == None or client_secret_input == None:
            client_id = request.json["client_id"]
            client_secret_input = request.json["client_secret"]'''

        # data = request.json
        print(f"Data: {client_id} {client_secret_input}")
        # print("Data: {} et {}".format(client_id, client_secret_input))
        # print("MES DONNEES ---------------->\n", data)

        # the client secret in the database is "hashed" with a one-way hash
        hash_object = hashlib.sha1(bytes(client_secret_input, 'utf-8'))
        hashed_client_secret = hash_object.hexdigest()

        # make a call to the model to authenticate
        authentication = authModel.authenticate(
            client_id, hashed_client_secret)
        if authentication == False:
            return jsonify({'successful created': False})
        else:
            return json.dumps(authentication, indent=4, sort_keys=True, default=str)
            # return {'success': True}
    else:
        return render_template("auth.html", name="auth")


if __name__ == '__main__':
    app.run(debug=True)
