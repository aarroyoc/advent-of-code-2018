import day6

def test_samples():
    max_finite_area,region_size = day6.day6("day6/prueba.txt")
    assert max_finite_area == 17

def test_stars():
    max_finite_area,region_size = day6.day6("day6/input.txt")
    assert max_finite_area == 5365
    assert region_size == 42513