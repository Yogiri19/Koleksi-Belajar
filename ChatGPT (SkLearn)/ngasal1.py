import os
os.system('cls')

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)
x = [[1, 2, 3], # 2 sample, 3 features
     [11, 12, 13]]
y = [0, 1] # classes of each sample
clf.fit(x,y)
print(clf)

from sklearn.preprocessing import StandardScaler
x = [[0, 15],
     [1, -10]]
# scale data according to computed scaling values
StandardScaler().fit(x).transform(x)
print(x)