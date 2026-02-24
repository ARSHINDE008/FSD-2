from flask import Flask
from routes.student_routes import student_bp
from config import config_dict

def create_app(config_name="default"):
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config_dict[config_name])

    # Register Blueprint
    app.register_blueprint(student_bp)

    return app

app = create_app()

@app.route("/")
def home():
    return {"message": "Backend Server is running"}

if __name__ == "__main__":
    app.run(debug=True)
