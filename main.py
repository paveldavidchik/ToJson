
from functools import wraps
import json


def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return json.dumps(data)
    return wrapper


@to_json
def get_data():
    return {'a': 15}


print(get_data())
