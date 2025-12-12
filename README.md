# Events API Lab

## Overview
This lab expands on RESTful write operations using Flask by introducing
input validation, reusable lookup logic, and consistent error handling.
The focus is on building reliable POST, PATCH, and DELETE endpoints while
maintaining clean, testable code.

---

## Project Structure

events-api-lab/
events-api-lab/app.py
events-api-lab/testing/
events-api-lab/testing/test_app.py
events-api-lab/pytest.ini
events-api-lab/README.md


- app.py contains the Flask application and route logic
- testing/test_app.py holds automated tests for each endpoint
- pytest.ini configures pytest to correctly locate application modules

## Application Overview
The Flask app provides three routes:

/events (POST)
- Accepts JSON input to create a new event.
- Validates that a non-empty title is provided.
- Automatically assigns a new ID to the event.
- Returns the created event with a 201 Created response.
- Returns a 400 Bad Request response if input is invalid.

/events/<event_id> (PATCH)
- Accepts JSON input to update the title of an existing event.
- Validates that a non-empty title is provided.
- Returns the updated event if found.
- Returns a 404 Not Found response if the event does not exist.
- Returns a 400 Bad Request response if input is invalid.

/events/<event_id> (DELETE)
- Removes an event from the in-memory list.
- Returns a 204 No Content response if successful.
- Returns a 404 Not Found response if the event does not exist.

All responses follow RESTful conventions and use JSON where applicable.

## Key Features
- RESTful write operations using POST, PATCH, and DELETE
- Input validation to prevent invalid data
- Reusable helper logic for event lookup
- Consistent error handling for missing resources
- Proper HTTP status code usage (201, 200, 204, 400, 404)
- In-memory data storage for testing purposes
- Automated testing using Flask’s test client and pytest

## Running the Tests

From the project root use the following:
- python -m pytest

## General project notes

Project passed through ChatGPT to identify logic issues, validate
RESTful behavior, and assist in refining validation and error-handling
patterns. The README.md was reviewed and edited for clarity,
consistency, and alignment with lab requirements prior to submission.
