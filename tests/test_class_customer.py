import pytest
import pandas as pd
import os
import sys
#print(sys.path)
sys.path.append(os.path.abspath('Python_Project/retail'))
from retail.class_customer import Customer


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
'''def test_avg_transaction_amount(sample_customer):
    # Since the total_spent() method returns a string instead of a numerical value, we need to parse it to a float before performing the assertion
    expected_avg_amount = float(sample_customer.total_spent()) / sample_customer.total_transactions()
    assert sample_customer.avg_transaction_amount() == expected_avg_amount'''
