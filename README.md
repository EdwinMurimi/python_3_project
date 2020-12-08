# python 3

## your name

<br>

<p>This project is a data science project that reads data from an online data source and displays the data to the user in dataframes.</p>

<br>

<p>In the program you are allowed to input a value which is the life expectancy of your choosing. the output is rows of data with a higher life expectancy than what you had put.</p>

<br>

<p>this line of code takes your input</p>

```python
    life_expentancy = int(input(
    "\ninput a minimum life expectancy value of your choice:\t"))

```

<p>The code for accessing the rows that satisfy the condition is shown below</p>

```python
    more_life_expectancy = pandas_dataframe    [pandas_dataframe['lifeExp'] > life_expentancy]

```

<br>

<p>The folowing code snippet output the data frames after the condition is satisfied</p>

```python
    print(more_life_expectancy)
```

<br>

> Steps to follow when running this program.

- download python 3 and install
- install pip in your system ( this is only for linux users )
- create a python file and write your program

  ```python

      import pandas as pd

      data_store = 'http://bit.ly/2cLzoxH'

      pandas_dataframe = pd.read_csv(data_store)


      print("\nThe full list of the countries is printed below:\n")
      print(pandas_dataframe)



      life_expentancy = int(input(
          "\ninput a minimum life expectancy value of your choice:\t"))

      more_life_expectancy = pandas_dataframe[pandas_dataframe['lifeExp']
                                              > life_expentancy]
      print("\n\nfull list of countries with a life expextancy greater than " +
          str(life_expentancy) + "\n")
      print(more_life_expectancy)

  ```

- after completing your program open your command prompt or terminal and type the following command:
  ```bash
      C:\Users\edwin\OneDrive\Desktop\New folder> python name_of_your_file.py
  ```
- finally, your output
