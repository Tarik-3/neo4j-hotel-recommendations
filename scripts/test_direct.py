"""
Comprehensive test script that doesn't require a running server
Tests the service functions directly
"""
import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from services_mock import get_best_hotels_mock

def test_egypt_hotels():
    """Test hotels for Egypt"""
    print("\n" + "="*60)
    print("TEST 1: Best Hotels for Egypt")
    print("="*60)
    
    hotels = get_best_hotels_mock("Egypt", limit=5)
    
    if not hotels:
        print("✗ FAIL: No hotels returned")
        return False
    
    print(f"✓ Found {len(hotels)} hotels")
    for i, hotel in enumerate(hotels, 1):
        print(f"\n{i}. {hotel['name']}")
        print(f"   Price: ${hotel['price']}/night")
        print(f"   Rating: {hotel['rating']}⭐")
        print(f"   Distance: {hotel['distance_km']} km")
        print(f"   Score: {hotel['score']}")
    
    return True

def test_price_filter():
    """Test price filtering"""
    print("\n" + "="*60)
    print("TEST 2: Morocco Hotels under $150")
    print("="*60)
    
    max_price = 150
    hotels = get_best_hotels_mock("Morocco", max_price=max_price)
    
    print(f"✓ Found {len(hotels)} hotels under ${max_price}")
    
    for i, hotel in enumerate(hotels, 1):
        if hotel['price'] > max_price:
            print(f"✗ FAIL: {hotel['name']} costs ${hotel['price']} (over ${max_price})")
            return False
        print(f"{i}. {hotel['name']} - ${hotel['price']}")
    
    print("✓ All hotels are within price range")
    return True

def test_limit():
    """Test limit parameter"""
    print("\n" + "="*60)
    print("TEST 3: Limit Results (Top 2 for Algeria)")
    print("="*60)
    
    limit = 2
    hotels = get_best_hotels_mock("Algeria", limit=limit)
    
    if len(hotels) != limit:
        print(f"✗ FAIL: Expected {limit} hotels, got {len(hotels)}")
        return False
    
    print(f"✓ Correctly returned {limit} hotels")
    for i, hotel in enumerate(hotels, 1):
        print(f"{i}. {hotel['name']} (Score: {hotel['score']})")
    
    return True

def test_score_sorting():
    """Test that results are sorted by score"""
    print("\n" + "="*60)
    print("TEST 4: Score Sorting (Senegal)")
    print("="*60)
    
    hotels = get_best_hotels_mock("Senegal")
    
    # Check if sorted by score (ascending)
    scores = [h['score'] for h in hotels]
    is_sorted = all(scores[i] <= scores[i+1] for i in range(len(scores)-1))
    
    if not is_sorted:
        print("✗ FAIL: Hotels are not sorted by score")
        return False
    
    print("✓ Hotels are correctly sorted by score (lower is better)")
    for i, hotel in enumerate(hotels, 1):
        print(f"{i}. {hotel['name']} - Score: {hotel['score']}")
    
    return True

def test_invalid_country():
    """Test invalid country"""
    print("\n" + "="*60)
    print("TEST 5: Invalid Country")
    print("="*60)
    
    hotels = get_best_hotels_mock("InvalidCountry")
    
    if len(hotels) == 0:
        print("✓ Correctly returned empty list for invalid country")
        return True
    else:
        print("✗ FAIL: Should return empty list for invalid country")
        return False

def test_combined_filters():
    """Test combined price filter and limit"""
    print("\n" + "="*60)
    print("TEST 6: Combined Filters (Egypt, max $120, limit 2)")
    print("="*60)
    
    hotels = get_best_hotels_mock("Egypt", max_price=120, limit=2)
    
    if len(hotels) > 2:
        print(f"✗ FAIL: Expected max 2 hotels, got {len(hotels)}")
        return False
    
    for hotel in hotels:
        if hotel['price'] > 120:
            print(f"✗ FAIL: {hotel['name']} costs ${hotel['price']} (over $120)")
            return False
    
    print(f"✓ Found {len(hotels)} hotels matching criteria")
    for hotel in hotels:
        print(f"  - {hotel['name']}: ${hotel['price']}")
    
    return True

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*70)
    print(" HOTEL RECOMMENDATION SYSTEM - DIRECT FUNCTION TESTS")
    print("="*70)
    
    tests = [
        ("Egypt Hotels", test_egypt_hotels),
        ("Price Filter", test_price_filter),
        ("Limit Parameter", test_limit),
        ("Score Sorting", test_score_sorting),
        ("Invalid Country", test_invalid_country),
        ("Combined Filters", test_combined_filters),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            passed = test_func()
            results.append((name, passed))
        except Exception as e:
            print(f"\n✗ {name} failed with error: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))
    
    # Print summary
    print("\n" + "="*70)
    print(" TEST SUMMARY")
    print("="*70)
    
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {name}")
    
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)
    
    print(f"\n📊 Total: {passed_count}/{total_count} tests passed ({passed_count*100//total_count}%)")
    
    if passed_count == total_count:
        print("🎉 All tests passed!")
    else:
        print(f"⚠️  {total_count - passed_count} test(s) failed")
    
    print("="*70)
    
    return passed_count == total_count

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
