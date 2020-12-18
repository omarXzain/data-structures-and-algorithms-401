from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_validation():
    actual = multi_bracket_validation('(){}')
    expected = True
    assert actual == expected

def test_multi_bracket_validation2():
    actual = multi_bracket_validation('({]})}')
    expected = False
    assert actual == expected

def test_multi_bracket_validation3():
    actual = multi_bracket_validation('({())))')
    expected = False
    assert actual == expected

def test_multi_bracket_validation4():
    actual = multi_bracket_validation('[({()})]')
    expected = True
    assert actual == expected