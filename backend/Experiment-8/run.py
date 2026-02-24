from app import app

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(
        host=app.config.get("HOST", "0.0.0.0"),
        port=app.config.get("PORT", 5000),
        debug=app.config.get("DEBUG", True)
    )