# # -*- coding: utf-8 -*-
"""Flask authentication with AWS Cognito IdP in USER_PASSWORD_AUTH authentication model"""

from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists


SECRET_KEY = env.str("SECRET_KEY", default="SuperComplexSecretKey")
DEBUG = env.bool("DEBUG", default=False)
TESTING = env.bool("TESTING", default=False)

# AWS Cognito specific variables
AWS_REGION = "eu-west-1"
COGNITO_AUTH_FLOW = 'USER_PASSWORD_AUTH'
COGNITO_USER_POOL_ID = env.str("COGNITO_USER_POOL_ID", default="eu-west-1_XXYYZZ")
COGNITO_CLIENT_ID = env.str("COGNITO_CLIENT_ID", default="ASDFG")
COGNITO_CLIENT_SECRET = env.str("COGNITO_CLIENT_SECRET", default="ZXCVBNM")
