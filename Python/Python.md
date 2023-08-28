# Intro to Python

## What is python?
Most popular programming language used by soft ware companies like google. 
It has fairly easy syntax therefore easier to learn. 

It is used for many different applications including:
- Websites' backend code - The code that runs on your server (Front end code is the code that runs on the device like a phone or a laptop)
- Data analysis and research purposes. 

## Installing Python
IDE - Integrated Development Environment. Is an environment that is used by programmers to test the program after building it in python. 
Debugger: Helps you to det rid of bugs

### Jupyter Notebook?
Is an alternative environment for writing and testing your program quickly instead of using the traditional IDE. Usually used in research and data analysis purposes. Simple to install using anaconda

#### 2 components of jupyter notebook
- JN server. The window on the left, if you close it, JN will close.
- Brower (User Interface): This can be chrome, safari, firefox etc, that is connected to the server. The code is written here  but executed in the server. This is like the GUI. 

Go to [ANACONDA](https://www.anaconda.com/download#downloads) and select your operating system (Windows, linux, Mac) to download the corresponding anaconda distribution. This process takes a while. 

To lauch Jupyter, Launch an application called *Anaconda Navigator*, find jupyter notebook and launch. 

## Creating your first program
Launch notebook and it will open in the browser. Select your working directory and start a project by selecting "New"

You can start typing python scripts as shown below.

![Alt text](image.png)

This is called a string. 

### What are variables?

This is assigning certain characters to a number or a command. Forexample, I can say, a = 2, b = 5. The character assigned to a certain number or command, or a string (it can be anything) is called the variable. 
```
a = 1
b = 2
c = "hello world"
d = a + b
```

It is also possible to assign a new variable to the same value, forexample f = 2, while b is also = 2. 

## Data Visualization
This is the first before data analysis
Gives you an intuitive undestanding of data and shows patterns that are hard to see

### Why Python
One of the most popular and the best data visualization platforms. Has many libraries for computing and analysis (eg matplotlib). 

### Why Matplotlib?
This is one of the most popular and best libraries for data visualization. There are others such as seaborn. 

### Why Pandas.
Pandas is a popular open-source library in Python specifically designed for data manipulation and analysis. It provides data structures and functions that make it easier to work with structured data, such as tables and time series, and perform various data analysis tasks. Pandas is widely used in data science, machine learning, and other analytical fields.
Data Structures: Pandas introduces two primary data structures, Series and DataFrame, that allow you to store and manipulate data in a tabular format.

[] **DataFrame:** A DataFrame is a 2-dimensional labeled data structure, similar to a table in a database or a spreadsheet. It consists of rows and columns, where each column can have a different data type.

[] **Data Manipulation:** Pandas provides powerful tools for filtering, transforming, aggregating, and reshaping data. It allows you to clean, preprocess, and reshape data before analysis.

[] **Indexing and Selection:** Pandas allows you to label and select data based on various conditions and criteria. It also supports hierarchical indexing for more advanced data organization.

[] **Reading and Writing Data:** Pandas supports reading and writing data from/to various file formats, including CSV, Excel, SQL databases, and more.

[] **Missing Data Handling:** Pandas provides methods to handle missing or NaN (Not a Number) values in your dataset.

[] **Time Series:** Pandas offers functionality for working with time series data, making it easier to analyze and manipulate data with temporal components.

[] **Data Visualization:** While not its primary focus, Pandas integrates well with data visualization libraries like Matplotlib and Seaborn, allowing you to create visualizations directly from your DataFrame