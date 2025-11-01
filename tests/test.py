from crs.min_pro import sub , mul , sum_list , is_event , is_positive,max_of_two

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

def test_is_positive():
    assert is_positive(5)== 'true'

def test_is_positive02():
    assert is_positive(0)== 'false'

def test_is_positive03():
    assert is_positive(-5)== 'false'
def test_is_positive04():
    assert is_positive(-7)== 'false'

def test_max_of_two():
    assert max_of_two(5,4)==5
def test_max_of_two02():
    assert max_of_two(3,8)==8
def test_max_of_two03():
    assert max_of_two(9,9)==9












