import day7

def test_samples():
    work,second = day7.day7("day7/prueba.txt")
    assert work == "CABDFE"

def test_stars():
    work,second = day7.day7("day7/input.txt")
    assert work == "JRHSBCKUTVWDQAIGYOPXMFNZEL"
    assert second == 975