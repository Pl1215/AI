
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

loanmain = pd.read_csv("LoanApproval.csv")
Loandata = loanmain.copy()

print(Loandata.head())

Loandata = Loandata.dropna(axis=0)

Loandata = Loandata.drop(['gender'], axis=1)

Loandata = pd.get_dummies(Loandata, drop_first=True)

# Loandata.dtypes

X = Loandata.drop('status_Y',axis=1)
Y = Loandata[['status_Y']]

logreg = LogisticRegression()

logreg.fit(X,Y)


ch=int(input("Credit History: "))
income = int(input("Income: "))
Loanamt = int(input("Loan Amount: "))
Married = int(input("Married? (1/0): "))


X_test = np.array([ch,income,Loanamt,Married])

X_test = X_test.reshape(1,-1)

Y = logreg.predict(X_test)

print("\nStatus: \n")
if Y >= 0.5 :
    print("Loan Approved")
else :
    print("Loan Rejected")