from crs.min_pro import sub , mul , sum_list , is_event

def test_sub():
    assert sub(8,3) == 5

def test_sub02():
    assert sub(11,6) == 5

def test_mul():
    assert mul(3,6) == 18
def test_mul01():
    assert mul(3,4) == 12

def test_add_list():
    assert sum_list([1,5,4]) ==10

def test_add_list02():
    assert sum_list([1,5,7]) ==13

def test_add_list03():
    assert sum_list([1,5,4]) ==10

def test_add_list04():
    assert sum_list([]) ==0

def test_is_event():
    assert is_event(2) == 'true'
def test_is_event02():
    assert is_event(7) == 'false'













