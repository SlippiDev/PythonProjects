from turtle import shape
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix
# Data Reading
data = pd.read_csv(r'C:\Users\ashan\OneDrive\Documents\GitHub\PythonProjects\Machine_Learning\reading_data\iris.csv')
print(data)

# Data Analysis

print(data.info())
print(data.shape)
print(data.head(20))
print(data.tail(20))
print(data.describe())
cormatrix = data.corr()
plt.subplots = data.corr()
sns.heatmap(cormatrix, annot = True)
plt.show()

# Data Visualization

data.plot(kind = 'kde', subplots = True, layout = (2,2), sharex = False, sharey = False)
plt.show()
scatter_matrix(data, diagonal='hist')
scatter_matrix(data, diagonal='kde')
plt.show()

# Data Preperation

array = data.values
print(array)

X = array[:, 0:4]
print(X.shape)

y = array[:, 4] # also write directly 4, same result
print(y)

from sklearn.model_selection import train_test_split as tts

X_tr, X_tst, Y_tr, Y_tst = tts(X, y, test_size=0.20, random_state=1)
 
print(X_tr, Y_tr, X_tst, Y_tst)
model = []

from sklearn.svm import SVC
model.append(SVC(gamma = 'auto'))
from sklearn.linear_model import LogisticRegression as lr
model.append(lr(solver = 'liblinear', multi_class='ovr'))
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as lda
model.append(lda())
from sklearn.neighbors import KNeighborsClassifier as knc
model.append(knc())
from sklearn.naive_bayes import GaussianNB as gnb
model.append(gnb())
import sklearn.model_selection as ms
print(model)
for i in model:
    results = ms.cross_val_score(i, X_tr, Y_tr, cv = 10, scoring = 'accuracy' )
    sum = 0
    for j in results:
        sum = sum + j
    avg = sum/len(results)
    print("The mean of 10 outcomes of accuracy result of" , i  , "is" , avg , "!")
"""
model.fit(X_tr, Y_tr)
predictions = model.predict(X_tst)
print('Prediction is {}'.format(predictions))
print("Cross Check Y Test {}".format(Y_tst))
plt.scatter(Y_tst, predictions)
plt.xlabel('actual')
plt.ylabel('predicted')
x_lim = plt.xlim()
y_lim = plt.ylim()
plt.plot(x_lim, y_lim, 'k--')
plt.show()

# plt.plot(X_tst, Y_tst)
plt.plot(Y_tst, predictions)
plt.xticks()
plt.yticks()
plt.show()
"""