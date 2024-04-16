from project.main import app

def test_home_route():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test_login_route():
    response = app.test_client().get("/principal/login")
    assert response.status_code == 200

def test_register_route():
    response = app.test_client().get("/principal/register")
    assert response.status_code == 200

def test_fake_route():
    response = app.test_client().get("/principal/fake")
    assert response.status_code == 200