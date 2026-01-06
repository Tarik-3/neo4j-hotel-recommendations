"""
Test script for the Hotel Recommendation API
Tests all endpoints with various scenarios
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8001"

def print_response(title, response):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    try:
        data = response.json()
        print(json.dumps(data, indent=2))
    except:
        print(response.text)

def test_root():
    """Test the root endpoint"""
    response = requests.get(f"{BASE_URL}/")
    print_response("Test 1: Root Endpoint", response)
    return response.status_code == 200

def test_health():
    """Test health check endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print_response("Test 2: Health Check", response)
    return response.status_code == 200

def test_best_hotels_egypt():
    """Test hotels for Egypt"""
    response = requests.get(f"{BASE_URL}/best-hotels?country=Egypt&limit=3")
    print_response("Test 3: Best Hotels for Egypt (Top 3)", response)
    return response.status_code == 200 and len(response.json()) > 0

def test_best_hotels_with_price_filter():
    """Test hotels with price filter"""
    response = requests.get(f"{BASE_URL}/best-hotels?country=Morocco&max_price=150")
    print_response("Test 4: Morocco Hotels under $150", response)
    data = response.json()
    # Verify all hotels are under max price
    all_under_price = all(hotel["price"] <= 150 for hotel in data)
    return response.status_code == 200 and all_under_price

def test_best_hotels_algeria():
    """Test hotels for Algeria"""
    response = requests.get(f"{BASE_URL}/best-hotels?country=Algeria&limit=5")
    print_response("Test 5: Best Hotels for Algeria", response)
    return response.status_code == 200

def test_best_hotels_senegal():
    """Test hotels for Senegal"""
    response = requests.get(f"{BASE_URL}/best-hotels?country=Senegal")
    print_response("Test 6: Best Hotels for Senegal", response)
    return response.status_code == 200

def test_invalid_country():
    """Test with invalid country"""
    response = requests.get(f"{BASE_URL}/best-hotels?country=InvalidCountry")
    print_response("Test 7: Invalid Country (should return 404)", response)
    return response.status_code == 404

def test_price_filtering():
    """Test strict price filtering"""
    response = requests.get(f"{BASE_URL}/best-hotels?country=Egypt&max_price=100")
    print_response("Test 8: Egypt Hotels under $100", response)
    if response.status_code == 200:
        data = response.json()
        all_under_price = all(hotel["price"] <= 100 for hotel in data)
        print(f"\n✓ All hotels under $100: {all_under_price}")
        return all_under_price
    return False

def run_all_tests():
    """Run all tests and print summary"""
    print("\n" + "="*60)
    print("HOTEL RECOMMENDATION API - TEST SUITE")
    print("="*60)
    
    tests = [
        ("Root Endpoint", test_root),
        ("Health Check", test_health),
        ("Egypt Hotels", test_best_hotels_egypt),
        ("Price Filter (Morocco)", test_best_hotels_with_price_filter),
        ("Algeria Hotels", test_best_hotels_algeria),
        ("Senegal Hotels", test_best_hotels_senegal),
        ("Invalid Country", test_invalid_country),
        ("Strict Price Filter", test_price_filtering),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            passed = test_func()
            results.append((name, passed))
        except Exception as e:
            print(f"\n✗ {name} failed with error: {e}")
            results.append((name, False))
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {name}")
    
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)
    
    print(f"\nTotal: {passed_count}/{total_count} tests passed")
    print("="*60)
    
    return passed_count == total_count

if __name__ == "__main__":
    try:
        success = run_all_tests()
        exit(0 if success else 1)
    except requests.exceptions.ConnectionError:
        print("\n✗ ERROR: Could not connect to API server")
        print("Make sure the server is running on http://127.0.0.1:8001")
        print("Start with: uvicorn app.main_flexible:app --port 8001")
        exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        exit(1)
