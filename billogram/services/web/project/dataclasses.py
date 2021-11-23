from dataclasses import dataclass


@dataclass
class DiscountCode:
    discount_code: str
    discount_value: int


@dataclass
class UserCreds:
    name: str
    username: str
    email: str
    discount_code: str