import json
import pytest
import action_network
import requests
from django.urls import reverse, resolve
from config.settings.local import ACTIONNETWORK_API_KEYS
from django.test import Client


@pytest.mark.django_db
def test_events_api_url_routed(admin_client):
    response = admin_client.get("/api/events/")
    assert response.status_code == 200
    assert response["content-type"] == "application/json"


def test_events_api_url_resolves():
    resolver = resolve("/api/events/")
    assert resolver.view_name == "event-list"


def test_get_returns_event_list(admin_client):
    events_api_response = admin_client.get("/api/events/")
    event_list = json.loads(events_api_response.content.decode("utf8"))
    assert all(
        [{"id", "title", "start", "url"} == event.keys() for event in event_list]
    )
