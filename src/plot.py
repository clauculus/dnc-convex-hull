import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import datasets 
from myConvexHull import myConvexHull

# print dataset available to choose
print()
print("Which dataset do you want?")
print("1. iris")
print("2. wine")
print("3. breast_cancer")

# assume that user input is always valid
print()
choice = int(input("Enter the number of your choice: "))
print()

data = datasets 

if (choice == 1):
    data = datasets.load_iris()
elif (choice == 2):
    data = datasets.load_wine()
else:
    data = datasets.load_breast_cancer()

# create a dataframe
df = pd.DataFrame(data.data, columns=data.feature_names) 
df['Target'] = pd.DataFrame(data.target) 
df.head()

# print the name of attributes
print("Attributes:")
for i in range (len(data.feature_names)):
    print(str(i+1) + ". " + str(data.feature_names[i]))
print()

# assume that user input is always valid
attribute1 = int(input("Enter the number of the first attribute: "))
attribute2 = int(input("Enter the number of the second attribute: "))

x = attribute1 - 1
y = attribute2 - 1

plt.figure(figsize=(10, 6))
colors = ['b','r','g']

title = str(data.feature_names[x]) + " vs " + str(data.feature_names[y])
plt.title(title)
plt.xlabel(data.feature_names[x])
plt.ylabel(data.feature_names[y])

for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[x,y]].values
    hull = myConvexHull(bucket.tolist()) # using the divide and conquer implementation of convex hull
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])

    for j in range(1, len(hull) + 1):
        if j == len(hull):
            j = 0 
        p0 = hull[j - 1]
        p1 = hull[j]
        plt.plot((p0[0], p1[0]), (p0[1], p1[1]), colors[i])

plt.legend()
plt.show() # show 