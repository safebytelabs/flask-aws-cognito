# # -*- coding: utf-8 -*-
"""Flask authentication with AWS Cognito IdP in USER_PASSWORD_AUTH authentication model"""


class Config(object):
    """Base config, uses staging settings"""
    AWS_REGION = "eu-west-1"
    COGNITO_USER_POOL_ID = "eu-west-1_GGFFHHJJ"
    COGNITO_CLIENT_ID = "utyiutyityityuituyity"
    COGNITO_CLIENT_SECRET = "fasdfasdfasdfasdfasdfasdfasdfasdfasdfdfasfasdfas"
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
