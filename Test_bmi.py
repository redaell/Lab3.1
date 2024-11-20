<<<<<<< HEAD
import lab2.bmi as BMI

def test_calc_bmi_underweight():
    expected = -1
    result = BMI.calculate_bmi(weight=37.0, height=1.80)
    assert(result == expected)

def test_calc_bmi_normalweight():
    expected = 0
    result = BMI.calculate_bmi(weight=65.0, height=1.80)
    assert(result == expected)

def test_calc_bmi_overweight():
    expected = 1
    result = BMI.calculate_bmi(weight=95.0, height=1.80)
    assert(result == expected)
=======
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
>>>>>>> df7c82d0eeaf159650082eda5acd96ee5cba3f6b
