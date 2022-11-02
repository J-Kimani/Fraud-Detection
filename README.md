# Fraud Detection Web Application
Fraud detection web app is tasked with determining whether a transaction is fraudulent or not. A python model is trained with data from kaggle: https://www.kaggle.com/ealaxi/paysim1/.
The dataset used is a synthetic on generating using Paysim as an approach to the problem. The model used is a random forest classifier which takes in the following values:
1. Length of transaction: represents a unit of time where 1 step equals 1 hour.
2. Amount transacted.
3. Type of transaction: might be cash in, cash out, debit, payment or transfer.
4. Initial balance before transaction.
5. Customer's balance after the transaction.
6. Initial recipient balance before the transaction.
7. Recipient's balance after the transaction.

The app returns Fraudulent transaction or normal transaction.
