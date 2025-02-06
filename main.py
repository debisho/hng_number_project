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

# Function to check if a number is perfect (Fix: Ensure 0 is not classified as perfect)
def is_perfect(n):
    return n > 0 and sum(i for i in range(1, abs(n)) if abs(n) % i == 0) == abs(n)

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    if n < 0:  # Armstrong numbers are only defined for non-negative integers
        return False
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

@app.get("/api/classify-number")
async def classify_number(number: str):  # Accept input as string for validation
    try:
        # Ensure the input is a valid integer
        if not number.lstrip('-').isdigit():
            raise ValueError(number)  # Pass the invalid input to the exception

        number = int(number)  # Convert to integer after validation
        properties = []

        # Classify the number
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 != 0 else "even")

        # Fetch fun fact (only for integers)
        fun_fact_url = f"http://numbersapi.com/{number}/math?json"
        fun_fact = requests.get(fun_fact_url).json().get("text", "No fact found")

        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),  # Now correctly handles 0
            "properties": properties,
            "digit_sum": sum(int(d) for d in str(abs(number))),  # Handle negatives correctly
            "fun_fact": fun_fact
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail={"number": str(e), "error": True, "message": "Invalid number format"}
        )
