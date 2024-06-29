from flask import jsonify, request, Blueprint
from ..service.product_service import create_product, get_all_products

