# pandas is a python module that is used in data science pr
import pandas as pd

data_store = 'http://bit.ly/2cLzoxH'

pandas_dataframe = pd.read_csv(data_store)


print("\nThe full list of the countries is printed below:\n")
print(pandas_dataframe)


# we create an input here
# the user will be prompted to input a particular country from several selections and the the population of the
# country will be displayed alongside the full table of countries.
life_expentancy = int(input(
    "\ninput a minimum life expectancy value of your choice:\t"))

more_life_expectancy = pandas_dataframe[pandas_dataframe['lifeExp']
                                        > life_expentancy]
print("\n\nfull list of countries with a life expextancy greater than " +
      str(life_expentancy) + "\n")
print(more_life_expectancy)
