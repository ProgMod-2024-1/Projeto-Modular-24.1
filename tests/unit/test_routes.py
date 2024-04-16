from project.main import app

def test_home_route():
    response = app.test_client().get("/")
    assert response.status_code == 302

def test_fake_route():
    response = app.test_client().get("/fake")
    assert response.status_code == 302