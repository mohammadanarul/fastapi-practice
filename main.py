from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'hello': 'hello world'}


@app.get('/products/')
def product_list():
    products = [
        {
            'id': 1,
            'title': 'product-1',
            'price': 1500,
            'brand': 'asus',
            'category': 'Laptop'
        },
        {
            'id': 2,
            'title': 'product-2',
            'price': 2000,
            'brand': 'apple',
            'category': 'Laptop'
        },
        {
            'id': 3,
            'title': 'product-1',
            'price': 2555,
            'brand': 'Dell',
            'category': 'Laptop'
        },
        {
            'id': 4,
            'title': 'product-1',
            'price': 3000,
            'brand': 'hp',
            'category': 'Laptop'
        }
    ]
    return {'products': products}

@app.get('/products/{id}')
def product_detail(id:  int):
    print('product',id)
    return {'product': {'id': id, 'title': f'product-{id}', 'price': 152+id}}
