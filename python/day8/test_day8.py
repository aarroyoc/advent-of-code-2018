import day8

def test_samples():
    metadata_sum,node_value = day8.day8("day8/prueba.txt")
    assert metadata_sum == 138
    assert node_value == 66

def test_stars():
    metadata_sum,node_value = day8.day8("day8/input.txt")
    assert metadata_sum == 42768
    assert node_value == 34348