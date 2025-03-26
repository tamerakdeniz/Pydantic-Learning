# class Product:
#
#     def __init__(self, name, price, in_stock):
#         self.name = name
#         self.price = price
#         self.in_stock = in_stock
#
# if __name__ == '__main__':
#     ornek_product = Product('Apple', 1.99, True)
#     print(ornek_product.in_stock)

from pydantic import BaseModel

class ProductPydantic(BaseModel):

    name: str
    price: float
    in_stock: bool

if __name__ == '__main__':
    external_data = {
        'name': 'Laptop',
        'price': "999.99",
        'in_stock': "True"
    }

    product = ProductPydantic(
        name=external_data.get('name'),
        price=external_data.get('price'),
        in_stock=external_data.get('in_stock')
    )

    print(type(product.name))
    print(type(product.price))
    print(type(product.in_stock))