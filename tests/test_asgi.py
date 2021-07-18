from mangum import Mangum

from app.api import handler


def test_handler():
    assert isinstance(handler, Mangum)
