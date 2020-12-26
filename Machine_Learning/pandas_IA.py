import pandas

print("Single dimension:\n")
print(pandas.Series([1,2,3,5]))

print("\n\n Two dimensions:\n")
print(pandas.DataFrame([[1,2,3],[4,5,6]]))
data = [[1,2,3],[4,5,6]]
print(pandas.DataFrame(data, columns = ["c1","c2","c3"], index = ["user1","user2"]))
data2 = {
    "c1":["a","b","c"],
    "c2":[1,2,3]
}
data_dict = {
    "c1":[1,4],
    "c2": [2,5],
    "c3":[3,6]
}
dataframe = pandas.DataFrame(data_dict)
print(dataframe)
print(dataframe["c2"])

iris = pandas.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(iris.shape)
print(iris.head())
print(iris[["sepal_length", "sepal_width"]].head())


indices = iris["species"] == "virginica"
print(indices)
