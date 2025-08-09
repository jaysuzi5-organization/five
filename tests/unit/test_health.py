def test_health(client):
    """Test the /health endpoint returns UP status."""
    response = client.get("/api/five/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}
