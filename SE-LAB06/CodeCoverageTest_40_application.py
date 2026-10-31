import pytest
from ride_share_fare import (
    extra_distance_fare,
    seats_and_bags_ok,
    pickup_status
)

# Extra distance fare tests

def test_unknown_cab():
    with pytest.raises(ValueError):
        extra_distance_fare("luxury", 10, "city", False)

def test_negative_distance():
    with pytest.raises(ValueError):
        extra_distance_fare("mini", -5, "city", False)

def test_included_distance():
    assert extra_distance_fare("sedan", 5, "city", False) == 0

def test_extra_distance_city():
    assert extra_distance_fare("mini", 10, "city", False) == 60

def test_extra_distance_outstation():
    assert extra_distance_fare("mini", 10, "outstation", False) == 90

def test_subscriber():
    assert extra_distance_fare("mini", 10, "city", True) == 24

def test_suv_subscriber():
    assert extra_distance_fare("suv", 15, "city", True) == 36

def test_large_extra_distance_city():
    assert extra_distance_fare("mini", 30, "city", False) == 500

def test_large_extra_distance_outstation():
    assert extra_distance_fare("mini", 30, "outstation", False) == 750

# Seats and bags tests

def test_wheelchair_limit():
    assert seats_and_bags_ok(2, 3, True) is True

def test_wheelchair_exceeded():
    assert seats_and_bags_ok(3, 1, True) is False

def test_passenger_limit():
    assert seats_and_bags_ok(5, 1, False) is False

def test_bag_limit():
    assert seats_and_bags_ok(2, 3, False) is False

def test_normal_ride():
    assert seats_and_bags_ok(3, 2, False) is True

# Pickup status tests

def test_pickup_on_time():
    assert pickup_status(10, True, False) == "on_time"

def test_pickup_delayed():
    assert pickup_status(0, True, False) == "delayed"

def test_pickup_missed():
    assert pickup_status(-10, True, False) == "missed"