import day9

def test_sample_1():
    assert day9.day9(9,25) == 32

def test_sample_2():
    assert day9.day9(10,1618) == 8317

def test_sample_3():
    assert day9.day9(13,7999) == 146373

def test_sample_4():
    assert day9.day9(17,1104) == 2764

def test_sample_5():
    assert day9.day9(21,6111) == 54718

def test_sample_6():
    assert day9.day9(30,5807) == 37305


def test_star_1():
    assert day9.day9(486,70833) == 373597

def test_star_2():
    assert day9.day9(486,7083300) == 2954067253