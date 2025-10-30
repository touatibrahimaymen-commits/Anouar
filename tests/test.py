from crs.min_pro import sub , mul

def test_sub():
    assert sub(8,3) == 5

def test_sub02():
    assert sub(11,6) == 5

def test_mul():
    assert mul(3,6) == 18
def test_mul01():
    assert mul(3,4) == 12