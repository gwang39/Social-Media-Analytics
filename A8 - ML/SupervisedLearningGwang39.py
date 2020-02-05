import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn import tree, metrics


def main():
    missing_values = ["NaN", "NaT", "nan"]

    dataset = pd.read_excel(open('SocialMediaInsightsforMachineLearning.xlsm', 'rb'), sheet_name='Key metrics', na_values=missing_values)
    dataset = dataset.drop('Post Message', axis = 1)
    dataset = dataset.drop('Posted', axis = 1)
    dataset['Weekend'], _ = pd.factorize(dataset['Weekend'])
    dataset['Type'], _ = pd.factorize(dataset['Type'])
    dataset['Weather'], _ = pd.factorize(dataset['Weather'])

    dataset['Impressions'] = [1 if x >= 1000 else 0 for x in dataset['Impressions']]
    y = dataset['Impressions']
    X = dataset.drop('Impressions', axis = 1 )


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

    print(df)

    print(classification_report(y_test, y_pred))


if __name__ == '__main__':
    main()



