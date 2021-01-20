from app.serializer.category_schema import category_schema
from app.services.http import build_api_response
from app.models import Category
from flask import current_app

from typing import Dict

def register_category(data: Dict):

    category = Category(name=data['name'])

    current_app.db.session.add(category)
    current_app.db.session.commit()

    return build_api_response(201, category_schema.dumps(category))
    