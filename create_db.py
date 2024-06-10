from app import app, db  # Replace with the actual name of your file

with app.app_context():
    db.create_all()
