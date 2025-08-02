from project import stop_loss, take_profit, reward_risk
import pytest

def test_stop_loss():
    assert stop_loss(150, 2, 1000, "long") == pytest.approx((147.00, 3.00 , 20.00))
    assert stop_loss(300, 3, 700, "short") == pytest.approx((309.00, 9.00, 21.00))
    with pytest.raises(ValueError):
        result = stop_loss(69, 7, 900, "yes")

def test_take_profit():
    assert take_profit(100, 10, 1000, "long") == pytest.approx((110.00, 10.00, 100.00))
    assert take_profit(200, 7, 2000, "short") == pytest.approx((186.00, 14.00, 140.00))
    with pytest.raises(ValueError):
        result = take_profit(8, 34, 67, "no")

def test_reward_risk():
    assert reward_risk(100, 115, 95, 10, "long") == pytest.approx((3.0, 15.00, 5.00, 150.00, 50.00))
    assert reward_risk(200, 180, 210, 5, "short") == pytest.approx((2.0, 20.00, 10.00, 100.00, 50.00))
    with pytest.raises(ValueError):
        result = reward_risk(238, 190, 234, 8, "cs50")