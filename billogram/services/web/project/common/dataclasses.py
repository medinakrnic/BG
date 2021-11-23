import re
from functools import partial
from typing import Any


class CamelcaseDataKey:
    def on_bind_field(self, field_name: str, field_obj: Any) -> None:
        if not field_obj.data_key:
            field_obj.data_key = _to_camel_case(field_name)


def _to_camel_case(field_name: str) -> str:
    _snake_case = re.compile(r"(?<=\w)_(\w)")
    _to_camel_case = partial(_snake_case.sub, lambda m: m[1].upper())

    return _to_camel_case(field_name)
