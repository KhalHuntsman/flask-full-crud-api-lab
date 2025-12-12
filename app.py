#!/usr/bin/env python3

# Author: Hunter Steele
# Date: 12/12/25
# Version: 1.1

"""
Flask application demonstrating basic RESTful write operations.

The app supports:
- Creating new events (POST)
- Updating existing events (PATCH)
- Deleting events (DELETE)

All data is stored in an in-memory list for testing purposes.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data model
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


@app.route("/events", methods=["POST"])
def create_event():
    """Create a new event from JSON input."""
    data = request.get_json()

    new_id = max(event.id for event in events) + 1 if events else 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    """Update the title of an existing event."""
    data = request.get_json()

    for event in events:
        if event.id == event_id:
            event.title = data["title"]
            return jsonify(event.to_dict())

    return jsonify({"error": "Event not found"}), 404


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    """Remove an event from the list."""
    for event in events:
        if event.id == event_id:
            events.remove(event)
            return "", 204

    return jsonify({"error": "Event not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
