import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        ans = func(*args, **kwargs)
        return json.dumps(ans)
    return wrapped


@to_json
def get_data():
    return {
        'data': 42
    }


get_data()  # вернёт '{"data": 42}'