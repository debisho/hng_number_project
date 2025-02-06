# HNG_Number_Project
A FastAPI-based API that classifies numbers based on various mathematical properties, including Armstrong number, prime number, odd/even, and provides fun facts using the Numbers API.

# Technologies Used
Python 3.12.1
FastAPI
Docker
AWS EC2 (for deployment)
GitHub

# Features
Classify a number as Armstrong, prime, odd/even.
Provides a fun fact using the Numbers API.
Exposes a public RESTful API deployed on AWS EC2.

# Setup and Installation
Clone the repository: git clone https://github.com/your-username/hng_number_project.git

Navigate into the project folder: cd hng_number_project

Install dependencies: pip install -r requirements.txt

Run the application locally: uvicorn main:app --reload

# Running the API Locally
API Endpoint: GET /api/classify-number?number=

Access the API at http://127.0.0.1:8000. You can test with the following command: curl http://127.0.0.1:8000/api/classify-number?number=371

Example Request and Response:
curl http://127.0.0.1:8000/api/classify-number?number=371

Example Response(in json format): { "number": 371, "is_prime": false, "is_perfect": false, "properties": [ "armstrong", "odd" ], "digit_sum": 11, "fun_fact": "371 is a narcissistic number." }

# Dockerizing the API
To create a Docker image for your API, ensure your project directory contains the following:
Dockerfile: Defines the environment for the API. requirements.txt: Lists all the dependencies.

Build the Docker image and run the container: docker build -t number-classification-api . docker run -d -p 8000:8000 number-classification-api

# Deploying to AWS EC2
The API is deployed on AWS EC2. SSH into the EC2 instance: ssh -i /path/to/key.pem ubuntu@<EC2_SSH_KEY>

Install Docker on EC2: sudo apt-get update sudo apt-get install docker.io sudo systemctl enable --now docker

Pull and Run Docker Container: Ensure that your Docker image is accessible either by pushing it to Docker Hub or by transferring the image to your EC2 instance. Run the Docker container: docker run -d -p 80:8000 number-classification-api

You can access the live version at:
http://your-public-ip/api/classify-number?number=371 License This project is licensed under the MIT License - see the LICENSE file for details.

# Automating with GitHub
Create a repository.


# Explanation of Sections:
- Technologies Used: List of tools and frameworks.
- Features: Key features of the API (number classification, fun facts).
- Setup and Installation: Instructions for setting up the project locally.
- Running the API Locally: How to run the API using uvicorn for testing purposes.
- Dockerizing the API: Instructions to containerize the project using Docker.
- Deploying to AWS EC2: Detailed steps on how to deploy the application to AWS EC2.
- Automating with GitHub: Steps on how to automate with github
