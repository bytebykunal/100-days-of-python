import pandas
import random


data = pandas.read_csv("data/french_words.csv")

data_dict = data.to_dict(orient="records")
words = random.choice(data_dict)
print(words)
print(words["French"])
print(words["English"])
    

