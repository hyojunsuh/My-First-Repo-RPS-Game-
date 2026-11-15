# this acts as the entry point for web app directory
# it will look here first



from flask import Flask

from web_app.routes.home_routes import home_routes
#from web_app.routes.book_routes import book_routes
#from web_app.routes.weather_routes import weather_routes



def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    #app.register_blueprint(book_routes)
    #app.register_blueprint(weather_routes)
    return app




# this will be only run when we run it in the command line, not during test
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)