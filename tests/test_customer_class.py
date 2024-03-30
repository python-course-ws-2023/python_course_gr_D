#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pytest
import pandas as pd
from class_customer import Customer


# Sample data for testing
sample_transactions = pd.DataFrame({
    'CustomerID': [1, 1, 2, 2, 3],
    'Quantity': [5, 10, 15, 20, 25],
    'UnitPrice': [2.5, 3.0, 4.5, 5.0, 6.5]
})
    
# Define a pytest fixture to set up a sample customer
@pytest.fixture
def sample_customer():
    customer_id = 1
    country = 'US'
    transactions = sample_transactions[sample_transactions['CustomerID'] == customer_id]
    return Customer(customer_id, country, transactions)

# Test total_transactions() method of the Customer class
def test_total_transactions(sample_customer):
    assert sample_customer.total_transactions() == 2

# Test total_spent() method of the Customer class
def test_total_spent(sample_customer):
    assert sample_customer.total_spent() == "$5.50"

# Test avg_transaction_amount() method of the Customer class
def test_avg_transaction_amount(sample_customer):
    assert sample_customer.avg_transaction_amount() == 2.75


# In[ ]:





# In[ ]:




