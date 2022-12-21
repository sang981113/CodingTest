import LCM

def test_LCM_gcd():
    assert LCM.gcd(10, 5) == 5
    assert LCM.gcd(255, 132) == 3

def test_LCM_lcm():
    assert LCM.lcm(14, 24) == 168

class TestSample:
    def test_LCM_gcd():
        assert LCM.gcd(10, 5) == 5
        assert LCM.gcd(255, 132) == 3

    def test_LCM_lcm():
        assert LCM.lcm(14, 24) == 168
