# # -*- coding: utf-8 -*-
"""Flask authentication with AWS Cognito IdP in USER_PASSWORD_AUTH authentication model"""

from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists


class Config(object):
    """Base config, uses staging settings"""
    AWS_REGION = "eu-west-1"
    COGNITO_USER_POOL_ID = env("COGNITO_USER_POOL_ID") or "eu-west-1_XXYYZZ"
    COGNITO_CLIENT_ID = env("COGNITO_CLIENT_ID") or "ASDFG"
    COGNITO_CLIENT_SECRET = env("COGNITO_CLIENT_SECRET") or "ZXCVBNM"
    COGNITO_AUTH_FLOW = 'USER_PASSWORD_AUTH'


class ProductionConfig(Config):
    """Production configuration settings"""
    SECRET_KEY = "muysecretquetecagasporlapataabajoenproduccion"


class DevelopmentConfig(Config):
    """Development configuration settings"""
    SECRET_KEY = "muysecretquetecagasporlapataabajoendesarrollo"


class TestingConfig(Config):
    """Testing configuration settings"""
    SECRET_KEY = "muysecretquetecagasporlapataabajoentesting"
