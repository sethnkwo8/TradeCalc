from project import stop_loss, take_profit, reward_risk, accumulator_core
import pytest
from unittest.mock import patch

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

def test_growth_rate_only():
    result = accumulator_core(
        stake=100,
        take_profit_tick=0.1,
        tick_duration=2,
        trades_per_day=5,
        ticks_per_trade=10,
        growth_rate=5
    )
    assert result["target_profit"] == 5.0
    assert result["growth_rate"] == 5.0
    assert result["compound_mode"] is False

def test_target_profit_only():
    result = accumulator_core(
        stake=200,
        take_profit_tick=0.1,
        tick_duration=1,
        trades_per_day=4,
        ticks_per_trade=10,
        target_profit=10
    )
    assert result["growth_rate"] == 5.0
    assert result["target_profit"] == 10.0
    assert result["compound_mode"] is False

@patch("project.growth_rate_exceeds", return_value=([5.0, 5.25, 5.51], 10.0, 3, 15))
def test_both_valid_inputs(mock_growth):
    result = accumulator_core(
        stake=100,
        take_profit_tick=0.1,
        tick_duration=2,
        trades_per_day=5,
        ticks_per_trade=10,
        growth_rate=10,
        target_profit=10
    )
    assert result["growth_rate"] == 10.0
    assert result["compound_mode"] is True

@patch("project.growth_rate_exceeds", return_value=([5.0, 5.25, 5.51], 5.0, 3, 15))
def test_mismatched_growth_and_target(mock_growth):
    with pytest.raises(ValueError):
        accumulator_core(
            stake=100,
            take_profit_tick=0.1,
            tick_duration=2,
            trades_per_day=5,
            ticks_per_trade=10,
            growth_rate=10,
            target_profit=5  # mismatch
        )

def test_no_growth_or_target():
    with pytest.raises(ValueError):
        accumulator_core(
            stake=100,
            take_profit_tick=0.1,
            tick_duration=2,
            trades_per_day=5,
            ticks_per_trade=10
            # No growth_rate or target_profit
        )
