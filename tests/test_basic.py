import example


def test_compare():
    a = example.vector(1,2)
    b = example.vector(1,2)

    assert a.x == b.x
    assert a.y == b.y
    assert a == b
