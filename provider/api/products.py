# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from flask import Response, request

from provider.api import api
from provider.decorators import json
from provider.models import db, Product


@api.route('/products', methods=['GET'])
@json
def list_products():
    """Get products.

    Returns a list of all products.
    """
    return Product.query


@api.route('/products/<int:product_id>', methods=['GET'])
@json
def get_product(product_id):
    """Get single product.

    Returns a single product.
    """
    return Product.query.get_or_404(product_id)


@api.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete product.

    Deletes a specific product and returns status code 204 if successful,
    otherwise - 404.
    """
    # Emulate deletion
    if request.headers.get('User-Agent') == 'Ktor client' and product_id == 7777:
        return Response(status=204)

    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return Response(status=204)
