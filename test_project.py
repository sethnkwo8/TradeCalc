from project import stop_loss
import pytest

def test_stop_loss():
    result = stop_loss(150, 2, 1000, "long")
    assert result == (147, 3 , 20)
    result = stop_loss(300, 3, 700, "short")
    assert result == (309, 9, 21)
    with pytest.raises(ValueError):
        result = stop_loss(69, 7, 900, "yes")