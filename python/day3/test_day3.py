import day3

def test_sample():
    overlaps, non_overlapping = day3.day3("day3/prueba.txt")
    assert overlaps == 4
    assert non_overlapping == 3

def test_stars():
    overlaps, non_overlapping = day3.day3("day3/input.txt")
    assert overlaps == 98005
    assert non_overlapping == 331