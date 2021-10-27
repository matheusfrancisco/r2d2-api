from unittest.mock import patch
from app.models.establishment import Establishment

@patch('app.models.establishment.Table.all')
def test_all(mocked_super):

    e = Establishment('mock', 'mock', 'mock')
    mocked_super.return_value = [
        { "id": "recH73JJvr7vv1234",
            "fields": {"SameField": 1234, "Value": "abc"},
            "createdTime": "2017-06-06T18:30:57.000Z",
        },
        {
            "id": "recyXhbY4uax4567",
            "fields": {"SameField": 456, "Value": "def"},
            "createdTime": "2017-06-06T18:30:57.000Z",
        },
        {
            "id": "recyXhbY4uax891",
            "fields": {"SameField": 789, "Value": "xyz"},
            "createdTime": "2017-06-06T18:30:57.000Z",
        },
    ]

    response = e.all_establishments()
    assert response == [
        {"SameField": 1234, "Value": "abc"},
        {"SameField": 456, "Value": "def"},
        {"SameField": 789, "Value": "xyz"}
    ]
