from flask import Flask, request, jsonify
from marshmallow import ValidationError

from eshop.businsess_logic.order_usecases import order_create, order_get_many, order_get_by_id
from eshop.businsess_logic.product_usecases import product_get_many, product_create
from eshop.data_access.product_repo import delete_by_id, get_by_id
from eshop.view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams
from eshop.view.product_shemas import ProductSchema, ProductGetManyParams

app = Flask(__name__)


@app.post("/api/v1/order")
def order_create_endpoint():
    try:
        order_create_dto = OrderCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        order = order_create(
            product_ids=order_create_dto['product_ids']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return OrderSchema().dump(order)


@app.get("/api/v1/order")
def order_get_many_endpoint():
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    order = order_get_many(
        page=order_get_many_params['page'],
        limit=order_get_many_params['limit'],
    )

    return OrderSchema(many=True).dump(order)


@app.get("/api/v1/order/<id>")
def order_get_by_id_endpoint(id):
    order = order_get_by_id(id)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)


@app.post("/api/v1/product")
def product_create_endpoint():
    """Добавить новый продукт"""
    data = request.get_json()

    try:
        # Получаем и валидируем данные из запроса с помощью схемы
        product_data = ProductSchema().load(data)
        product = product_create(product_data['name'], product_data['price'])

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(ProductSchema().dump(product)), 201


@app.get("/api/v1/product")
def product_get_many_endpoint():
    """Просмотреть отдельный список продуктов"""
    try:
        product_get_many_params = ProductGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    product = product_get_many(
        page=product_get_many_params['page'],
        limit=product_get_many_params['limit'],
    )

    return ProductSchema(many=True).dump(product)


@app.get("/api/v1/product/<id>")
def product_get_by_id_endpoint(id: str):
    """Просмотреть отдельный продукт по id"""
    product = get_by_id(id)

    if product is None:
        return {
            "message": 'Not found'
        }, 404

    return ProductSchema().dump(product)


@app.delete("/api/v1/product/<id>")
def product_delete_by_id_endpoint(id: str):
    """Удалить отдельный продукт по id"""
    try:
        delete_by_id(id)
        return "Продукт удален", 200
    except Exception as ex:
        return f"Не удалось удалить продукт: {ex}", 404


def run_server():
    app.run(debug=True)
