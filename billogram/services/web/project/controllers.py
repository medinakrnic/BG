from flask import json, jsonify, request

from . import app
from .schemas import DiscountCodesSchema, UsersSchema
from .services import (
    check_claimed_discount_codes,
    check_user_discount_codes,
    generate_discount_code_list,
    get_discount_codes,
    get_users,
)


@app.route("/discount-codes", methods=["GET"])
def get_all_discount_codes():
    return json.dumps(DiscountCodesSchema(many=True).dump(get_discount_codes()))


@app.route("/users", methods=["GET"])
def get_all_users():
    return json.dumps(UsersSchema(many=True).dump(get_users()))


@app.route("/generate-discount-codes", methods=["POST"])
def create_discount_codes():
    discount_value = request.form['discount-value']
    discount_codes = request.form['discount-codes']
    return jsonify(generate_discount_code_list(int(discount_value), int(discount_codes)))


@app.route("/user/discount-code", methods=["GET"])
def get_user_discount_code():
    user_id = request.args.get("user-id", type=str)
    return jsonify(check_user_discount_codes(user_id))


@app.route("/check-claimed-discount-codes", methods=["GET"])
def get_loyalty_information():
    return json.dumps(UsersSchema(many=True).dump(check_claimed_discount_codes()))
