# write a function that takes a string argument and returns the no of vowels in it.

# def vowel_count(string):
#     vowels= ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     for ch in string.lower():
#         if ch in vowels:
#             count +=1
#     return count
#
# def test_with_my_name():
#     assert vowel_count('carlos kidman') == 4
#
# def test_with_my_uppercase_name():
#     assert vowel_count('KARLOS KIDMAN') == 4


# import pytest
# def test_file1_method1():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed"
# 	assert x == y,"test failed"
# def test_file1_method2():
#
#
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed"


#
# import pytest
# @pytest.mark.set1
# def test_file1_method1():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed"
# 	assert x == y,"test failed because x=" + str(x) + " y=" + str(y)
#
# @pytest.mark.set2
# def test_file1_method2():
# 	x=5
# 	y=7
# 	assert x+1 == y,"test failed"

import pytest

#start with test
#end with test
def test_m11():
    name= "selenium"
    assert name.upper() == "SELENIUM"
