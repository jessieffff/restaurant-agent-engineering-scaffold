from collections.abc import Generator
from xml.etree import ElementTree

import pytest
from fastapi.testclient import TestClient

from restaurant_agent.main import create_app


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(create_app()) as test_client:
        yield test_client


def test_restaurant_page_loads_without_claiming_a_booking(client: TestClient) -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "Juniper &amp; Stone" in response.text
    assert 'id="menu-grid"' in response.text
    assert 'id="hours-list"' in response.text
    assert 'id="reservation-form"' in response.text
    assert 'id="chat-dialog"' in response.text
    assert 'id="reservation-submit" type="submit" disabled' in response.text
    assert 'id="chat-message" rows="2" placeholder="Ask Juniper a question" disabled' in (
        response.text
    )
    assert 'id="chat-send" type="button" disabled' in response.text
    assert "Demo restaurant" not in response.text
    assert "no real bookings" not in response.text
    assert "Online availability is coming soon." in response.text


@pytest.mark.parametrize(
    ("path", "content_type"),
    [
        ("/assets/site.css", "text/css"),
        ("/assets/site.js", "text/javascript"),
        ("/assets/seasonal-table.svg", "image/svg+xml"),
    ],
)
def test_website_assets_are_served(
    client: TestClient,
    path: str,
    content_type: str,
) -> None:
    response = client.get(path)

    assert response.status_code == 200
    assert response.headers["content-type"].startswith(content_type)
    assert response.content
    if path.endswith(".svg"):
        assert ElementTree.fromstring(response.content).tag.endswith("svg")


def test_website_keeps_api_routes_and_rejects_posting_a_booking(client: TestClient) -> None:
    assert client.get("/health/live").status_code == 200
    assert client.get("/docs").status_code == 200
    assert "/" not in client.get("/openapi.json").json()["paths"]
    assert client.post("/", data={"date": "2026-10-16"}).status_code == 405
