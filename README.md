# DS_Rappi_Challenge-

In this repo, you can find my answers to the RappiPay challenge for Data Scientists.

In this notebook, [Rappi_challenge.ipynb](https://github.com/Juanes8/DS_Rappi_Challenge-/blob/main/Rappi_challenge.ipynb), you can find the EDA of the data, as well as the models used. During the Exploratory Data Analysis, it was detected the dataset was unbalanced, there are null values in the *establecimiento* and *ciudad* variables that were change as *Unknown*. The distribution of the variables was almost the same for the fraudulent transactions and not a fraud. There is no clear correlation between the variables, and the customers were classified into 3 clusters based the *linea_tc*.

It seems that at 23:00 there are more frauds, compare to other hours. From 17:00 the frauds tent to rise compare to the morning, but at 7:00 there is peak. The distributions of the users transactions, frauds and fraud_rate are exponential and look similar. The mean of transactions per user is around 6. The users with the higher fraud rate are the ones with less transactions, this something that was expected.

The models used were, Logistic Regression, Decision Tree, Random Forest, CatBoost and XGBoost. As the dataset was unbalanced the models did not perform well, so another approach was proposed. To solve the unbalanced dataset, it was decided to sample more data from the fraud transactions to have more data from these. This approach was better as the models improved in their performance having the best of all XGBoost. The metrics to evaluate the models were Precision, AUC and training time. 

Then it were obtained the best hyperparameters for the model using [Optuna](https://optuna.org/). The hyperparameters that maxime the AUC are the following:
|Hyperparameter|value|
|--|--|
|n_estimators|5854|
|max_depth|6|
|learning_rate|0.1777|
|reg_alpha|0.8928|
|reg_lambda|6.1056|


The most important features of the best model were: 
- *genero_Unknown*
- *tipo_tc_Virtual*
- *ciudad_Merida*
- *os_*

This model is not the best to deploy into production yet, it is capable of detecting most fraudsters. The ideal of course is to have more data from the fraudulent transactions and not to abuse the resampling method. Another approach is to have more data from each record to have more variables and have a more robust model.

The best model can be found as [xgb.pkl](https://github.com/Juanes8/DS_Rappi_Challenge-/blob/main/xgb.pkl). In [model.py](https://github.com/Juanes8/DS_Rappi_Challenge-/blob/main/model.py) is a simple Flask API that is used to put into production the model. It can be tested using the [validation.json](https://github.com/Juanes8/DS_Rappi_Challenge-/blob/main/validation.json) file, and to use it just run

```{python}
python model.py
```

The prediction will be display through ```https://localhost:8080/predict```.

The packages used for this challenge can be found in [requirements.txt](https://github.com/Juanes8/DS_Rappi_Challenge-/blob/main/requirements.txt)

This is the structure of this repo 
```
.
├── README.md
├── Rappi_challenge.ipynb     # Notebook with EDA and experiments of models                                
├── model.py                  # Flask API for model                
├── xgb.pkl                   # Final model                          
├── requirements.txt          # Packages used                      
├── validation.json           # JSON file to validate the production of the model
```
