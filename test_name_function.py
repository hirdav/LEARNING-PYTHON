from name_function import get_formatted_name 
def test_first_last_name():
    """do names like John hopkins work"""
    formatted_name = get_formatted_name('John','Hopkins')
    assert formatted_name == 'John Hopkins'