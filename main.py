from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

@app.get("/api/classify-number")
async def classify_number(number: int):
    try:
        number = int(number)
        properties = []

        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 != 0 else "even")

        # Get fun fact from Numbers API
        fun_fact_url = f"http://numbersapi.com/{number}/math?json"
        response = requests.get(fun_fact_url)
        fun_fact = response.json().get("text", "No fact found")

        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(int(d) for d in str(number)),
            "fun_fact": fun_fact
        }
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": "alphabet", "error": True})

