import pandas as pd
import numpy as np

def freq_table(x, print_tab = True):
    '''
        Function to get frequency table
        Input: x, Series
           print_tab, whether to save results as pd.DataFrame
    '''
    frequency_table = {}
    for item in x:
        frequency_table[item] = frequency_table.get(item, 0) + 1

    # Print the frequency table
    if print_tab:
        for item, count in frequency_table.items():
            print(f"{item}: {count}")
    else:
        columns = ['Code', 'Quantity']
        my_table = pd.DataFrame(columns=columns)
        for item, count in frequency_table.items():
            data = [{'Code':item, 'Quantity':count }]
            data_frame_to_append = pd.DataFrame(data)
            my_table = pd.concat([my_table, data_frame_to_append], ignore_index=True)
        return my_table
            

def print_missing_values(df):
    '''
    Finds missing values and pronts how many and their pecentage
    '''
    missing_values_count = df.isnull().sum()  # Count missing values in each column
    total_values = len(df)  # Total number of rows in the DataFrame

    print("Missing Values:")
    for column, missing_count in missing_values_count.items():
        if missing_count > 0:
            missing_percentage = (missing_count / total_values) * 100
            print(f"{column}: {missing_count} missing values, {missing_percentage:.2f}%")
        else:
            print(f"{column}: No missing values")



#It is quicker
#can set a function 
def remove_spaces(arr):
  '''
new loop
we rmeove extra spaces
firstly save than split than join back
extra check on float, because nan are floats
'''
  dat_arr = pd.Series(arr)
  dat_arr = dat_arr.str.split()
  for i in range(len(dat_arr)):
    if  not isinstance(dat_arr[i], float):
      dat_arr[i] = ' '.join(list(dat_arr[i]))
  return dat_arr
#easy to make test 


def remove_double_names(data):
    '''
remove double names, we choose most frequent name 
'''
    stock = data['StockCode'].unique()
    for i in range(len(stock)):
        arr = data.loc[data['StockCode'] == stock[i]]['Description'].unique()
        #remove double names
        if  (sum(pd.Series(arr).isna()) == 1 and len(arr) > 2) or (sum(pd.Series(arr).isna()) == 0 and len(arr) > 1) or (len(arr) >= 2):
            tab = freq_table(data.loc[data['StockCode'] == stock[i]]['Description'].dropna(), print_tab = False)
            new_ind = tab.loc[tab["Quantity"] == tab["Quantity"].max(), "Code"].reset_index(drop=True)[0]
            #print(new_ind)
            needed_len = len(data.loc[data['StockCode'] == stock[i]]['Description'])
            data.loc[data['StockCode'] == stock[i], 'Description'] = np.array([new_ind for x in range(needed_len)])
            #print(data.loc[data['StockCode'] == stock[i], 'Description'].unique())
    return data