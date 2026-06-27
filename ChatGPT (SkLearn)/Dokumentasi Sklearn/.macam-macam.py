import os
os.system('cls')

1. # Regression
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor

2. # Classification
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

3. # Clustering
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

4. # PREPROCESSING
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import PolynomialFeatures

5. # FEATURE SELECTION
from sklearn.feature_selection import SelectKBest, chi2, RFE

6. # PIPELINE
from sklearn.pipeline import Pipeline

7. # DIMENSION REDUCTION
from sklearn.decomposition import PCA

8. # DATASET BAWAAN
from sklearn.datasets import load_iris, load_digits, load_boston

9. # UTILITY TAMBAHAN
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer