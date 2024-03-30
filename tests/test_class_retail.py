import pytest
import pandas as pd
import os
import sys
#print(sys.path)
sys.path.append(os.path.abspath('Python_Project/retail'))
import retail.class_retail as cr

sample_string = " Postcard  with flowers"

def test_remove_spaces():
    assert remove_spaces(sample_string) == "Postcard with flowers"
