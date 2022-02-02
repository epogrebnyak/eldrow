from eldrow import correct_spot, just_contains


def test_just_contains():
    assert just_contains(hidden="shale", guess="saify") == ".a..."


def test_correct_spot():
    assert correct_spot(hidden="chart", guess="shale") == "_ha__"
