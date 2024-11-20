import Lab2_prac.bmi as bmi

def test_bmi_normal_weight():
    expected = 0
    result = bmi.calculate_bmi(weight=57, height=1.62)
    assert(result==expected)
    
def test_bmi_over_weight():
    expected = 1
    result = bmi.calculate_bmi(weight=90, height=1.62)
    assert(result==expected)
    
def test_bmi_under_weight():
    expected = -1
    result = bmi.calculate_bmi(weight=30, height=1.62)
    assert(result==expected)