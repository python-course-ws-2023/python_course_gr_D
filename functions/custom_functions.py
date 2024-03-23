import numpy as np
import polars as pl
import re
import os

#Attribute sw: likely Descriptions that are used, but are not meaningfull
#this attribute can be set in to the other value  

class retail:

    # Stop words - likely comments are used in Description column
    sw = ['?', '??', '???', 'check', 'found', 'amazon', 'damaged', 'damages', 'amazon', 
     'crushed', 'sold as set on dotcom', 'water damage', 'Found', 'missing','???lost',
     'AMAZON', 'Damaged', 'counted', 'wet pallet', '????missing','Water damaged', 'adjustment', 
     'dotcom', 'mouldy, thrown away.', 'Show Samples', 'lost', 'incorrectly made-thrown away.', 're-adjustment',
     'damages/dotcom?', 'sold as set/6 by dotcom', 'cracked', 'crushed ctn','taig adjust no stock',
     'POSSIBLE DAMAGES OR LOST?', "Dotcom sold in 6's", "sold in set?", 'reverse 21/5/10 adjustment',
     "can't find", "?missing", '?? missing', 'amazon adjust', 'Dotcom set', 'wrongly sold as sets', 
      '?sold as sets?', 'mouldy, unsaleable.', 'Amazon', 'faulty', 'rcvd be air temp fix for dotcom sit',
     're dotcom quick fix.', 'Dotcom sales', 'missing?','reverse 21/5/10 adjustment', 
      'incorrectly put back into stock', 'damages?','had been put aside', 'wet boxes', 'wet rusty',
     'sold as set on dotcom', '????damages????', 'historic computer difference?....se', 
     'smashed', 'had been put aside', 'dotcomstock','mixed up', 'michel oops', 'test', 'lost in space',
     'amazon sales','FOUND', 'thrown away', 'wet pallet', '???missing', 'Water damaged', 'FBA',
     'dotcom sales', 'Dotcom', 'Dotcom sales', 'Damages/samples', 'on cargo order', 'adjustment', 'dotcom',
     'damages?', 'mystery! Only ever imported 1800', 'MIA', 'wet', 'samples', 'sold as set on dotcom and amazon', 
     'sold as 1', 'MERCHANT CHANDLER CREDIT ERROR, STO', 'OOPS ! adjustment','Missing', '?lost', 
      'found some more on shelf', 'reverse previous adjustment','Amazon sold sets', 'dotcom sold sets',
     'mix up with c', 'wrongly sold sets',  '? sold as sets?', 'damages/display', 'Not rcvd in 10/11/2010 delivery',
      'Amazon Adjustment', 'CHECK', 'damaged stock', 'showroom', 'found box', 'stock check', 'barcode problem',
     'Found in w/hse', 'damages/credits from ASOS.', 'damages?', 'damages/showroom etc', 'had been put aside',
      'DAMAGED', 'sold as 1', '?missing', 'taig adjust', 'Wet pallet-thrown away', 'Had been put aside.',
      'did  a credit  and did not tick ret', 'damages wax', 'thrown away', 'damages?', 'Adjustment', '?display?',
      'WET/MOULDY', 'adjust', 'damages wax', 'returned', 'mixed up', 'crushed', 'label mix up', 'lost??',
      'Sold as 1 on dotcom', 'sold as set by dotcom', 'smashed', 'Dagamed', 'water damaged', 'wrong barcode',
      'check?', 'wet/rusty', 'Thrown away.', 'ebay', 'thrown away', 'crushed boxes', 'stock creditted wrongly', 
      'stock check', 'wet damaged', 'test', 'samples/damages', 'to push order througha s stock was',
      'Unsaleable, destroyed.', 'wet damaged', 'Given away', 'wet?', 'Printing smudges/thrown away',
      'printing smudges/thrown away', 'thrown away',  'had been put aside', 'rusty throw away', 'Crushed',
      'mailout','temp adjustment', 'allocate stock for dotcom orders ta', 'add stock to allocate online orders', 
      'for online retail orders', 'website fixed', 'Breakages', 'smashed', 'wet damaged', 'incorrect stock entry.',
      'Lighthouse Trading zero invc incorr', 'Incorrect stock entry.','mouldy',
      'alan hodge cant mamage this section', 'incorrectly credited C550456 see 47' 
    ]
    

    def __init__(self, target_path, data_file, remove_sw = False):
        """Read, preprocess, and plot Online retail data.

        Parameters
        ----------
        target_path : str
            local working directory where data should be stored.
        data_file : str
            name of file to which data should be saved.
        remove_sw = False : bool
            indicates, whether all rows, where description contains stop 
            words must be rmeoved after preprocessing 

        Returns
        -------
        cwd : str
            Information about the current working directory.
        summary_stats : DataFrame
            Summary statistics of the Online retail data.
        plot : plt.plot
            Plot of the Online retail data.

        """
        self.target_path = target_path
        self.data_file = data_file
        self.remove_sw = remove_sw
        
    def __call__(self):

        # set current working directory   
        self.set_cwd(self.target_path)
        # read data set
        data = self.read_data(self.data_file)
        #preprocess data set
        data = self.data_preprocessed(data)

        self.get_summary(data)
  
  
    def set_cwd(self, target_path):
        """Set current working directory to desired local path

        Parameters
        ----------
        target_path : str
            local path that should be used as current working directory.

        Returns
        -------
        current_working_directory : str
            Prints current working directory.

        """
        # set the current working directory 
        os.chdir(target_path)
        
        # get current working directory
        current_wd = os.getcwd()
        return print("current working directory:", current_wd)
    
           
    def read_data(self,  data_file):
        """Reads data from a CSV file into a Polars DataFrame.

        Parameters
        ----------
        data_file : str
            The name of the CSV file containing the data.

        Returns
        -------
        data : polars.DataFrame
            A Polars DataFrame containing the data read from the CSV file.
        """
        data = pl.read_csv(data_file, dtypes = {'InvoiceNo': pl.String})
        return data
        
 
    def remove_spaces(self, arr):
        """Removes extra spaces from a string.

        Parameters
        ----------
        arr : str
            Input string containing extra spaces.
    
        Returns
        -------
        str
            String with extra spaces removed.
        """
        dat_arr = " ".join(arr.split(" "))
        return dat_arr
    
    def find_match(self, s):
        """Searches for specific patterns in a string. Here used to find descriptions 
           that contain information about broken products.

        Parameters
        ----------
        s : str
            Input string to search for patterns.

        Returns
        -------
        bool
            True if any of the specified patterns are found in the string, False otherwise.
        """
        pattern1 = re.compile(r'\bwrong', re.IGNORECASE) 
        pattern2 = re.compile(r'code') 
        pattern3 = re.compile(r'debt') 
        pattern4 = re.compile(r'Marked') 
        pattern5 = re.compile(r'207') 

        return (re.search(pattern1, s) or re.search(pattern2, s) or 
                                       re.search(pattern4, s) or re.search(pattern3, s) or
                                      re.search(pattern5, s))
    

    def find_stopWords(self, word, sw = sw):
        """Checks if a word is a stop word.

        Parameters
        ----------
        word : str
            The string to check.
        sw : list, optional
            List of stop words. Default is the variable `sw`.

        Returns
        -------
        str or None
            The input word if it is a stop word, otherwise None.
        """
        if word in sw: 
            return word
        else:
            return None
    
    def replace_stopWords(self, word, sw = sw):
        """Replaces stop words with None.

        Parameters
        ----------
        word : str
            The string to check.
        sw : list, optional
            List of stop words. Default is the variable `sw`.

        Returns
        -------
        str or None
            None if the input word is a stop word, otherwise the input word.
        """
        if word in sw: 
            return None
        else:
            return word
        
    def most_frequent(self, descriptions):
        """Finds the most frequent element in a list of descriptions.

        Parameters
        ----------
        descriptions : List[str]
            List of descriptions.

        Returns
        -------
        str or None
            The most frequent description in the list. If the list is empty, returns None.
        """
        descriptions = descriptions.drop_nans().to_list()
        if not descriptions:
            return None
        return max(set(descriptions), key=descriptions.count)

    def data_preprocessed(self, data):
        """preprocess data 

        Parameters
        ----------
        data_file : str
            name of locally saved data file.

        Returns
        -------
        df_joined : polars.DataFrame
            Preprocessed data set with 84 observations and 6 variables (subject, 
            gender, scenario, attitude, frequency, mean_pitch).
        summaries : polars.DataFrame
            Mean pitch value grouped by attitude (informel, polite) and gender 
            (female, male).

        """
        data = data.with_columns(pl.col("Description").map_elements(self.remove_spaces))
        #removed wrong codes
        data = data.with_columns(pl.col('Description').map_elements(lambda x: self.find_match(x)).alias("matches"))
        data = data.filter(pl.col('matches').is_null()).drop('matches')

        data = data.with_columns(pl.col('Description').map_elements(self.find_stopWords).alias('addition'))
        data = data.with_columns(pl.col('Description').map_elements(self.replace_stopWords))
        if self.remove_sw:
            data = data.filter(pl.col('addition').is_null())#.drop('addition')

        grouped = data.groupby('StockCode').agg(pl.col('Description').alias("temp"))
        grouped = grouped.with_columns(pl.col('temp').map_elements(self.most_frequent).alias('Description')).drop("temp")
        data = data.drop('Description').join(grouped, on = 'StockCode') 
        data = data.filter(~pl.col('Description').is_null(),  pl.col('Quantity')> 0, pl.col('UnitPrice')>0)
        data = data.with_columns(pl.col("InvoiceNo").cast(pl.Int32).alias('InvoiceNo'))

        return (data)
    
    def get_summary(self, data):
        """Generate a summary of the dataset including various statistics.

        Parameters
        ----------
        data :  polars.DataFrame
            Input  polars.DataFrame containing the dataset.

        Returns
        -------
        None
            Prints the summary of the dataset including the following statistics:
            - Number of unique invoice codes
            - Number of unique stock codes
            - Average number of stock codes per invoice
            - Average quantity per stock code
            - Number of unique customer IDs
            - Country with the most stock codes
        """

        # Number of unique invoice codes
        unique_invoice_codes = data['InvoiceNo'].n_unique()

        # Number of unique stock codes
        unique_stock_codes = data['StockCode'].n_unique()

        # Average number of stock codes per one invoice code
        avg_stock_codes_per_invoice = data.group_by('InvoiceNo').agg(pl.count('StockCode')).select(pl.col('StockCode').mean()).get_columns()[0][0]

        # Average quantity per stock code
        avg_quantity_per_stock_code = data.group_by('StockCode').agg(pl.mean('Quantity')).select(pl.col('Quantity').mean()).get_columns()[0][0]

        # Number of unique customer IDs
        unique_customer_ids = data['CustomerID'].n_unique()

        # Countries where there are at most unique invoice  codes
        countries_with_most_stock_codes = data.group_by('Country', 'InvoiceNo').agg(pl.count('StockCode')).group_by('Country').agg(pl.count('InvoiceNo')).sort(by = 'InvoiceNo', descending = True).get_columns()[0][0]

        # Display the summary
        print("Summary of the Dataset:\n")
        print(f"Number of Unique Invoice Codes: {unique_invoice_codes}")
        print(f"Number of Unique Stock Codes: {unique_stock_codes}")
        print(f"Average Number of Stock Codes per Invoice: {avg_stock_codes_per_invoice:.2f}")
        print(f"Average Quantity per Stock Code: {avg_quantity_per_stock_code:.2f}")
        print(f"Number of Unique Customer IDs: {unique_customer_ids}")
        print(f"Country with Most Stock Codes: {countries_with_most_stock_codes}")

    
