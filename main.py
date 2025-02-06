from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is perfect (supports negative numbers)
def is_perfect(n):
    return sum(i for i in range(1, abs(n)) if abs(n) % i == 0) == abs(n)

# Function to check if a number is an Armstrong number (only for non-negative integers)
def is_armstrong(n):
    if n < 0 or not n.is_integer():  # Armstrong numbers are not defined for negatives or decimals
        return False
    digits = [int(d) for d in str(int(n))]  # Convert to integer before checking
    return sum(d ** len(digits) for d in digits) == int(n)

@app.get("/api/classify-number")
async def classify_number(number: float):  # Accept float instead of int
    try:
        properties = []

        # Classify number
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if int(number) % 2 != 0 else "even")

        # Fetch fun fact
        fun_fact_url = f"http://numbersapi.com/{int(number)}/math?json"  # Convert to int for API
        fun_fact = requests.get(fun_fact_url).json().get("text", "No fact found")

        return {
            "number": number,
            "is_prime": is_prime(int(number)),  # Convert to int for prime check
            "is_perfect": is_perfect(int(number)),  # Convert to int for perfect number check
            "properties": properties,
            "digit_sum": sum(int(d) for d in str(int(abs(number)))),  # Handle negatives correctly
            "fun_fact": fun_fact
        }

    except ValueError:
        raise HTTPException(status_code=400, detail={"number": "Invalid input", "error": True})
