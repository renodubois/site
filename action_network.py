import requests
from django.conf import settings
from events.models import Event
from datetime import datetime


def get_events():
    def get_events_for_formation(formation_key):
        events_response = requests.get(
            "https://actionnetwork.org/api/v2/events/",
            # params={"filter": f"modified_date gt '{last_api_call}'"},
            headers={"OSDI-API-Token": formation_key},
        )
        events_json = events_response.json()
        return events_json["_embedded"]["osdi:events"]

    return [
        get_events_for_formation(key)
        for key in settings.ACTIONNETWORK_API_KEYS.values()
    ]


def save_events(events):
    for event in events:
        obj, created = Event.objects.update_or_create(
            id=event["identifiers"][0].split(":")[1],
            defaults={
                "title": event["title"],
                "start": datetime.fromisoformat(event["start_date"][:-1]),
                "url": event["browser_url"],
                "description": event["description"],
            },
        )
    return


def get_emails():
    messages_response = requests.get(
        "https://actionnetwork.org/api/v2/messages/",
        headers={"OSDI-API-Token": settings.ACTIONNETWORK_API_KEYS["main"]},
    )
    events_json = messages_response.json()
    return events_json["_embedded"]["osdi:messages"]