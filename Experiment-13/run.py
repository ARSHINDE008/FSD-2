"""
Student Management API - Run Script
Simplified script to run the Flask application with database initialization
"""

import os
import sys
from app import app, db

def run_app():
    """Initialize database and run Flask app"""
    print("\n" + "=" * 60)
    print("Student Management API - Starting Server")
    print("=" * 60)
    
    try:
        # Create application context
        with app.app_context():
            print("✓ Application context created")
            
            # Create all tables
            db.create_all()
            print("✓ Database tables initialized")
        
        # Start Flask server
        print("\n" + "-" * 60)
        print("🚀 Server is running at: http://localhost:5000")
        print("📚 API Documentation: See README.md")
        print("📮 Postman Collection: Experiment-13.postman_collection.json")
        print("-" * 60 + "\n")
        
        app.run(
            debug=True,
            host='0.0.0.0',
            port=5000,
            use_reloader=True
        )
    
    except Exception as e:
        print(f"\n✗ Error starting server: {e}")
        sys.exit(1)
    finally:
        print("\n" + "=" * 60)
        print("Server stopped")
        print("=" * 60)

if __name__ == "__main__":
    run_app()
