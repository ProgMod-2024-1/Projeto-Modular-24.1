from project.main import app

def test_home_route():
    response = app.test_client().get("/")
    assert response.status_code == 302

def test_register_route():
    response = app.test_client().get("/")
    assert response.status_code == 302

def test_login_route():
    response = app.test_client().get("/")
    assert response.status_code == 302

def test_filial_route():
    response = app.test_client().get("/")
    assert response.status_code == 302