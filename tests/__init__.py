import pytest
import json
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_no_arguments(client):
    response = client.get("/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "error" in data
    assert "usage" in data


def test_handle_a_command(client):
    response = client.get("/?a=2023/07")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "a" in data
    assert "Highest Average" in data["a"]
    assert "Lowest Average" in data["a"]
    assert "Mean Humidity" in data["a"]


def test_handle_c_command(client):
    response = client.get("/?c=2023/07")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "c" in data
    assert "Data" in data["c"]
    assert "Date" in data["c"]


def test_handle_e_command(client):
    response = client.get("/?e=2023")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "e" in data
    assert "Highest" in data["e"]
    assert "Lowest" in data["e"]
    assert "Max Humidity" in data["e"]


def test_multiple_arguments(client):
    response = client.get("/?a=2023/07&c=2023/07&e=2023")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "a" in data
    assert "c" in data
    assert "e" in data
