import pytest
import requests

# The base URL of the website
BASE_URL = "https://www.factorial-calc.com"

def test_positive_factorial():
    # Test calculating the factorial of a positive integer
    response = requests.get(f"{BASE_URL}/factorial?number=5")
    assert response.status_code == 200
    assert int(response.content) == 120

def test_factorial_of_zero():
    # Test calculating the factorial of zero
    response = requests.get(f"{BASE_URL}/factorial?number=0")
    assert response.status_code == 200
    assert int(response.content) == 1

def test_non_integer_input():
    # Test handling a non-integer input value
    response = requests.get(f"{BASE_URL}/factorial?number=2.5")
    assert response.status_code == 400
    assert b"Error: Input must be an integer." in response.content

def test_negative_input():
    # Test handling a negative input value
    response = requests.get(f"{BASE_URL}/factorial?number=-5")
    assert response.status_code == 400
    assert b"Undefined: Negative factorial is not defined." in response.content

def test_large_input():
    # Test handling a large input value
    response = requests.get(f"{BASE_URL}/factorial?number=1000000")
    assert response.status_code == 400
    assert b"Error: Input value is too large." in response.content

def test_large_integer_value():
    # Test calculating the factorial of a large integer value
    response = requests.get(f"{BASE_URL}/factorial?number=50")
    assert response.status_code == 200
    assert int(response.content) == 30414093201713378043612608166064768844377641568960512000000000000
