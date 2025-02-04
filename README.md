# Number API

A FastAPI-based API that classifies numbers based on various mathematical properties, including Armstrong number, prime number, odd/even, and provides fun facts using the Numbers API.

## Technologies Used
- Python 3.12.1
- FastAPI
- Docker
- AWS EC2 (for deployment)
- GitHub

## Setup and Installation

1. Clone the repository:
   git clone https://github.com/your-username/number-classification-api.git

2. Navigate into the project folder:
cd number-api

3. Install dependencies:
pip install -r requirements.txt

4. Run the application locally:
uvicorn main:app --reload

5. API Endpoint
GET /api/classify-number?number=<number>

Example Request: curl http://127.0.0.1:8000/api/classify-number?number=371
Example Response(in json format):
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": [
    "armstrong",
    "odd"
  ],
  "digit_sum": 11,
  "fun_fact": "371 is a narcissistic number."
}

6. Deployment
The API is deployed on AWS EC2. You can access the live version at:

http://44.202.42.122/api/classify-number?number=371
License
This project is licensed under the MIT License - see the LICENSE file for details.
