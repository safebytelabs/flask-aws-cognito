# # -*- coding: utf-8 -*-
"""Flask authentication with AWS Cognito IdP in USER_PASSWORD_AUTH authentication model"""

import base64
import hashlib
import hmac
# import json

import boto3
from flask import Flask, jsonify, request
from botocore.exceptions import ClientError


app = Flask(__name__)
app.config.from_object("src.cognito.config.ProductionConfig")
app.json.sort_keys = False  # type: ignore
cognito_client = boto3.client('cognito-idp', region_name=app.config['AWS_REGION'])


def get_secret_hash(username):
    """
    Generate the secret hash using the username, client ID, and client secret.
    https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#cognito-user-pools-computing-secret-hash
    """
    message = username + app.config['COGNITO_CLIENT_ID']
    key = bytes(app.config['COGNITO_CLIENT_SECRET'], 'latin-1')
    msg = bytes(message, 'latin-1')
    dig = hmac.new(key, msg, digestmod=hashlib.sha256).digest()
    return base64.b64encode(dig).decode()


@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint
    """
    username = request.json.get("username")
    password = request.json.get("password")
    secret_hash = get_secret_hash(username)

    try:
        # Initiate the authentication process
        auth_response = cognito_client.initiate_auth(
            ClientId=app.config['COGNITO_CLIENT_ID'],
            AuthFlow=app.config['COGNITO_AUTH_FLOW'],
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password,
                'SECRET_HASH': secret_hash
            }
        )

        # print(json.dumps(auth_response))

        # If authentication is successful, return the tokens
        if auth_response and 'AuthenticationResult' in auth_response:
            return jsonify({
                'message': 'Authentication successful',
                'id_token': auth_response['AuthenticationResult']['IdToken'],  # We want this token...
                'access_token': auth_response['AuthenticationResult']['AccessToken'],  # ...but we don't want this other
                'refresh_token': auth_response['AuthenticationResult']['RefreshToken'],  # this is for life span
            }), 200
        else:
            # If authentication fails something happened with credentials and/or the username hash
            return jsonify({'message': 'Authentication failed'}), 401
    except ClientError as e:
        # This means AWS is responding with an error because we didn't provide the right credentials
        return jsonify({'message': e.response['Error']['Message']}), 400


if __name__ == '__main__':
    app.run(debug=True, port=8888)
