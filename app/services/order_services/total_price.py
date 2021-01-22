from app.models import Product

def total_price(products_id: list) -> float:
    products_price = list()

    for product_id in products_id:
        product = Product.query.filter(Product.id == product_id).first()
        products_price.append(product.price)

    return sum(products_price)