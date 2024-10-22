#Student: Junayd Lateef (ASU ID: 1221505571)

import pandas as pd
from sklearn.model_selection import train_test_split # used to split the data
from sklearn import metrics #get functions for accuracy, precision, recall, and f1 score
from sklearn import tree # import decision tree


#grab information from database
heart = pd.read_csv("heart_failure.csv")

#separate data from their labels/classifiers
data = heart.iloc[:, 0:-1]
targets = heart.iloc[:, -1]

#split the data into 75-25 (training/testing)
data_train, data_test, t_train, t_test = train_test_split(data, targets, train_size=0.70, test_size=0.30, random_state=0)

#training model - Decision Tree Classification
model_list = [tree.DecisionTreeClassifier(criterion='gini', max_depth=2, random_state=0),                   #Trial 1
              tree.DecisionTreeClassifier(criterion = "gini",  max_depth = 4, random_state=0),           #Trial 2
              tree.DecisionTreeClassifier(criterion='entropy', max_depth=2, random_state=0),                #Trial 3
              tree.DecisionTreeClassifier(criterion = "entropy",  max_depth = 4, random_state=0),        #Trial 4
              tree.DecisionTreeClassifier(criterion='log_loss', max_depth=2, random_state=0),               #Trial 5
              tree.DecisionTreeClassifier(criterion = "log_loss",  max_depth = 4, random_state=0)]       #Trial 6

#Metric value lists
metric_list = [] #displays all the percentages so they can be compared in 'results.py'
f1_list = [] #displays all the f1 scores and compares them separately in 'results.py'

for i, x in enumerate(model_list):
    #Train model
    model = x.fit(data_train, t_train)

    #testing model - Decision Tree Classification
    pred = model.predict(data_test)

    #determine results
    accuracy = metrics.accuracy_score(t_test, pred)
    precision = metrics.precision_score(t_test, pred, average='weighted')
    recall = metrics.recall_score(t_test, pred, average='weighted')
    f1_score = metrics.f1_score(t_test, pred, average='weighted')
    
    metric_list.append((float(accuracy), float(precision), float(recall)))
    f1_list.append(float(f1_score))

    #now we save the Decision tree to see what splits are made
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(20, 8))
    tree.plot_tree(model, feature_names=data.columns, impurity=True,
                   class_names=["1", "0"], filled=True)
    plt.savefig("./70_30_DecisionTrees/70_30_Trial" + str(i + 1) + ".png")

print(metric_list)
print(f1_list)