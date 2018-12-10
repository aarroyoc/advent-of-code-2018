import day5

def test_stars():
    units,minimum = day5.day5("day5/input.txt")
    assert units == 10584
    assert minimum == 6968