Installation

Create a virtual environment and install dependencies:

pip install -r requirements.txt

---

Running the Application

From the project root:

uvicorn src.main:app --reload

The API will be available at:

http://127.0.0.1:8000

---

API
Health Check

GET /

Response:

{
  "message": "Bridge Service Running"
}
Execute Action

POST /actions

Request:

{
  "action": "scroll"
}

Response:

{
  "status": "success",
  "action": "scroll"
}

Example:

curl -X POST \
http://127.0.0.1:8000/actions \
-H "Content-Type: application/json" \
-d '{"action":"scroll"}'