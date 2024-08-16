import requests
import json
import pytest

API_KEY = '1dbd2d09demsh1466da92bf53cc6p121ddbjsn61447eb3d301'
API_HOST = 'yh-finance.p.rapidapi.com'
BASE_URL = 'https://yh-finance.p.rapidapi.com/market/v2/get-quotes'

def getHeaders(apiKey, apiHost):
    return {
        'X-RapidAPI-Key': apiKey,
        'X-RapidAPI-Host': apiHost,
    }

def getParams(symbols):
    return {
        "symbols": symbols
    }

def getRequest(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    return response

def assertOK(response):
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def validateStructure(expected, actual):
    if isinstance(expected, dict):
        assert isinstance(actual, dict), f"Expected dict, but got {type(actual)}"
        for key, value in expected.items():
            assert key in actual, f"Missing key: {key}"
            validateStructure(value, actual[key])
    elif isinstance(expected, list):
        assert isinstance(actual, list), f"Expected list, but got {type(actual)}"
        for item in actual:
            validateStructure(expected[0], item)
    else:
        expectedType = {
            "string": str,
            "boolean": bool,
            "number": (int, float)
        }[expected]
        assert isinstance(actual, expectedType), f"Expected {expected}, but got {type(actual).__name__}"

def test_contractGetQuotes():
    headers = getHeaders(API_KEY, API_HOST)
    params = getParams("BTC-USD")

    # GET Request
    response = getRequest(BASE_URL, headers=headers, params=params)
    assertOK(response)

    # Load expected JSON response from file
    with open('expectedGetQuote.json', 'r') as file:
        expectedStructure = json.load(file)
    
    # Get JSON response
    responseJson = response.json()

    # Validate response structure
    validateStructure(expectedStructure, responseJson)

    # Print response scheme
    print(responseJson)

