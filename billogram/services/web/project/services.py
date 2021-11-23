import random
import string
from typing import Optional

from . import db
from .dataclasses import DiscountCode, UserCreds
from .models import DiscountCodes, Users


def get_discount_codes():
    query = DiscountCodes.query.all()
    for result in query:
        yield (
            DiscountCode(
                discount_code=result.discount_code,
                discount_value=result.discount_value,
            )
        )


def get_users():
    query = Users.query.all()
    for result in query:
        yield (
            UserCreds(
                name=result.name,
                username=result.username,
                email=result.email,
                discount_code=result.discount_code,
            )
        )


def generate_discount_code_list(discount_value: int, discount_codes: int) -> list:
    generated_discount_codes = []
    for i in range(discount_codes):
        generated_discount_code = f"BRAND{discount_value}-" + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=5)
        )
        discount_code_exists = DiscountCodes.query.filter(
            DiscountCodes.discount_code == generated_discount_code
        ).first()
        if discount_code_exists:
            return "discount code exists"
        else:
            generated_discount_codes.append(generated_discount_code)
            db.session.add(
                DiscountCodes(
                    discount_code=generated_discount_code, discount_value=discount_value
                )
            )
            db.session.commit()
    return generated_discount_codes


def check_user_discount_codes(user_id: str) -> Optional[str]:
    user = Users.query.filter(Users.user_id == user_id).first()
    if not user:
        return "This user does not exist in our system."

    if user.discount_code:
        return "This user has already received a discount code."
    else:
        discount_code = DiscountCodes.query.filter(
            DiscountCodes.user_claimed == None
        ).first()
        user.discount_code = discount_code.code_id
        discount_code.user_claimed = user.user_id
        db.session.commit()
        return discount_code.discount_code


def check_claimed_discount_codes() -> Optional[str]:
    claimed_discount_codes = DiscountCodes.query.filter(
        DiscountCodes.user_claimed != None
    ).all()

    if not claimed_discount_codes:
        return "No discount codes have been claimed."

    for claimed_discount_code in claimed_discount_codes:
        user = Users.query.filter(
            Users.user_id == claimed_discount_code.user_claimed
        ).first()

        yield (
            UserCreds(
                name=user.name,
                username=user.username,
                email=user.email,
                discount_code=user.discount_code,
            )
        )
