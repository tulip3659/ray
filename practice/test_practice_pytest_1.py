"""
This is a practice file on pytest
"""
# The below two lines are used to import module from another file
import pytest
import sys
sys.path.insert(0, '/Users/babakaghazadeh/repos/ray/practice/')
from practice_capitalize import capitalize_this

def test_capitalize_this():
    assert capitalize_this("babak")=="Babak"

def test_raises_a_type_error_on_numbers():
    with pytest.raises(TypeError):
        capitalize_this(9)