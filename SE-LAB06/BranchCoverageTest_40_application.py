import pytest
from ride_share_fare import (
    extra_distance_fare,
    seats_and_bags_ok,
    pickup_status
)

# Extra distance fare branches

def test_invalid_cab():
    with pytest.raises(ValueError):
        extra_distance_fare("luxury", 10, "city", False)

def test_negative_distance():
    with pytest.raises(ValueError):
        extra_distance_fare("mini", -1, "city", False)

def test_non_subscriber_city():
    assert extra_distance_fare("mini", 10, "city", False) == 60

def test_subscriber_non_suv():
    assert extra_distance_fare("mini", 10, "city", True) == 24

def test_subscriber_suv():
    assert extra_distance_fare("suv", 15, "city", True) == 36

def test_no_extra_distance():
    assert extra_distance_fare("mini", 5, "city", False) == 0

def test_large_extra_city():
    assert extra_distance_fare("mini", 30, "city", False) == 500

def test_large_extra_outstation():
    assert extra_distance_fare("mini", 30, "outstation", False) == 750

def test_large_extra_other_zone():
    assert extra_distance_fare("mini", 30, "suburb", False) == 650

# Seats and bags branches

def test_wheelchair_passengers_allowed():
    assert seats_and_bags_ok(2, 3, True) is True

def test_wheelchair_passengers_not_allowed():
    assert seats_and_bags_ok(3, 1, True) is False

def test_more_than_four_passengers():
    assert seats_and_bags_ok(5, 1, False) is False

def test_bags_exceed_limit():
    assert seats_and_bags_ok(3, 3, False) is False

def test_passengers_and_bags_allowed():
    assert seats_and_bags_ok(3, 2, False) is True

# Pickup status branches

def test_scheduled_non_airport_on_time():
    assert pickup_status(10, True, False) == "on_time"

def test_unscheduled_airport_on_time():
    assert pickup_status(15, False, True) == "on_time"

def test_unscheduled_non_airport_on_time():
    assert pickup_status(5, False, False) == "on_time"

def test_scheduled_airport_on_time():
    assert pickup_status(20, True, True) == "on_time"

def test_pickup_delayed():
    assert pickup_status(0, True, False) == "delayed"

def test_pickup_missed():
    assert pickup_status(-10, True, False) == "missed"