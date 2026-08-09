from .conftest import client

def test_create_student():

    payload = {
        "name": "Dheerendra",
        "email": "abc@gmail.com"
    }

    response = client.post(
        "/students",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Dheerendra"

    assert data["email"] == "abc@gmail.com"