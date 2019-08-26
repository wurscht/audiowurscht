import pytest
import psycopg2
import requests
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.db import connections
from django.contrib.auth.models import User


def run_sql(sql):
    conn = psycopg2.connect(database='test_database')
    conn.set_isolation_leel(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()


@pytest.yield_fixture(scope='session')
def django_db_setup():
    from django.conf import settings

@pytest.mark.django_db
def test_logout():
    me = User.objects.get(username='Test')
    data = {
        'username': 'Test'
    }
    requests.post('http://localhost:8000/logout/', data=data)
    import pdb; pdb.set_trace()
    assert not me.is_authenticated
