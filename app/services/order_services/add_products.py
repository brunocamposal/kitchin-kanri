from app.models import Product

def add_products(order, products_id: list) -> None:

    for product_id in products_id:
        product = Product.query.filter(Product.id == product_id).first()
        order.products_list.append(product)