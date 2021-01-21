from app.models import Product

def verify_product(products_id: list) -> None:
    for product_id in products_id:
        product = Product.query.filter(Product.id == product_id).first()
        
        if product is None:
            return "Produto não cadastrado"

    return None