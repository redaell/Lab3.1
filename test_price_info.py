import price_info as pi

def test_cost_of_fruit():
    fruit = "apple"
    quantity = 10
    expected = 12
    result = pi.cost_of_fruits(fruit, quantity)
    assert(result == expected)

def test_total_cost_shopping():
    pi.quantity_list = {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}
    expected = 46.75
    result = pi.total_cost_shopping()
    assert (result == expected)