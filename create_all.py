from app import create_app
from app.models import db

if __name__ == "__main__":
    db.create_all(app=create_app())
