from app.models import db
from app import create_app

if __name__ == "__main__":
    db.create_all(app=create_app())
