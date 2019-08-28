import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user():
    me = User.objects.get(username='Test')
    assert me.first_name == "Test"
    assert me.is_active
