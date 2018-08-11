import os
from flask import Flask

def create_app(test_config = None):
    #create and config the app
    app = Flask(__name__,instance_relative_config = True)
    print(app.instance_path)
    app.config.from_mapping(
            SECRET_KEY = 'dev',
            DATABASE = os.path.join(app.instance_path,'flaskr.sqlite')
            )
    if test_config is None :
        # when not testing
        app.config.from_pyfile("config.py",silent = True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello wang PX'

    return app
if __name__ == "__main__":
    create_app()
