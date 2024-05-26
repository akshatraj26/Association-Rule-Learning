# Apriori

# Importing the libraries
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("Market_Basket_Optimisation.csv", header=None)

transactions = []
for i in range(0, 7501):
    transactions.append([str(df.values[i, j]) for j in range(0, 20)])
    

col2 = df.loc[1, :].values

# transactions = []
# for i in range(0, 7501):
#     transactions.append(list(df.loc[i,:].values))


# product bought 3 times a day and 21 times week and then divide by total number of observation
min_support = 3 * 7 / 7500

# Training Apriori on dataset
from apyori import apriori
rules = apriori(
    transactions, 
    min_support = min_support , 
    min_confidence = 0.2,
    min_lift = 3, min_length = 2)


# Visualizing the results
results = list(rules)

print(results[:2])

## Putting the results well organised into a Pandas DataFrame
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

## Displaying the results non sorted
resultsinDataFrame

## Displaying the results sorted by descending lifts
resultsinDataFrame.nlargest(n = 10, columns = 'Lift')