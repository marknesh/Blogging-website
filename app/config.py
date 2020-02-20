import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mike:Markmunene18@localhost/blogs'

    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")



class ProdConfig(Config):


    pass


class DevConfig(Config):

    debug=True



config_options={
    'development':DevConfig,
    'production': ProdConfig
}