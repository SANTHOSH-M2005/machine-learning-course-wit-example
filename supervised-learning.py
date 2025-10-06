from sklearn.tree import DecisionTreeClassifier

# Sample dataset: [weight, sweetness]
X = [[150, 7], [170, 6], [140, 8], [200, 4], [210, 3], [190, 5]]
y = ["Apple", "Apple", "Apple", "Orange", "Orange", "Orange"]

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict a new fruit
print(model.predict([[160, 7]]))  # Example new fruit
