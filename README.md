
# Python Retail Data Analysis Project

![License](https://img.shields.io/badge/license-MIT-blue.svg)

The Python Retail Data Analysis Project aims to provide retail businesses with tools for insightful analysis of customer behaviors and sales patterns. By utilizing advanced data manipulation and analysis techniques, this project seeks to unveil hidden insights within retail data, aiding strategic decision-making and fostering business growth.

## About The Project

This project was made by TU Dortmund University students Emona Bakalova, Mariia Hrechyn, Alican Ohkay for the final project of the Introduction to Python course. Understanding customer preferences and identifying sales trends are crucial components of success in the fast-paced retail industry. This project introduces a robust framework for the analysis of retail data, featuring classes such as `Customer` and `Retail`. These classes facilitate the examination of purchase histories, the evaluation of product performance, and the identification of significant sales trends.

- The `Customer` class delves into individual customer behaviors, revealing insights into purchase patterns, frequencies, and preferences.
- The `Retail` class offers a comprehensive overview of sales data, encompassing product performance, seasonal trends, and overall sales effectiveness.

  Source for Data;

  [Kaggle](https://www.kaggle.com/datasets/thedevastator/online-retail-transaction-records/code)

  
Python scripts and Jupyter notebooks are utilized to explore various aspects of retail data, from detailed analyses of customer behaviors to overarching examinations of sales trends.

## Getting Started

To begin utilizing the Python Retail Data Analysis Project, follow these steps to set up your environment:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/EmonaBakalova/Python_Project.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Python_Project
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

This project provides functionalities to analyze retail data, simplifying the process of gaining insights into customer behavior and sales performance.

### Analyzing Customer Data

Utilize the `Customer` class to analyze customer data, which enables the loading of customer data, analysis of purchasing patterns, and generation of reports.

```python
from retail.class_customer import Customer

# Load customer data
customer_data = Customer('docs/source/example/Online_Retail.csv')

# Display customer summary
print(customer_data.summary())
```

### Sales Analysis

The `Retail` class allows for a more extensive analysis of sales data, including the examination of trends and product performance.

```python
from retail.class_retail import Retail

# Load sales data
sales_data = Retail('docs/source/example/Online_Retail.csv')

# Analyze sales performance
print(sales_data.analyze_performance())
```

Refer to the included Jupyter notebooks for detailed examples and advanced usage scenarios:
- `class_customer.ipynb` for insights into the `Customer` class.
- `showcase.ipynb` for a comprehensive analysis using both the `Customer` and `Retail` classes.

## Contributing

Contributions to the Python Retail Data Analysis Project are highly appreciated. Follow these steps to contribute:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'')
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.
