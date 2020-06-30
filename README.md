# airbnb-data-modeling
libraries: numpy, pandas, lightgbm, matplotlib, scikit learn, scipy, warnings
Data can be found at https://www.kaggle.com/airbnb/seattle files calendar.csv, listings_seattle.csv
Airbnb day prices in Seattle are predicted using feature engineering, random forest and light gradient boosting feature selection and regression. These models aim to help hosts establish appropriate rental prices and also to find out what features can influence rental price the most. Text features such as name and description are also considered. 
Here we also compare random forest and light gradient boosting performance. Light Gradient Boosting (LGB) is relatively fast algorithm comparing with other boosting methods. In the final test the sum of two LGB models was applied to reduce overfitting. Final best R2 score on test is 0.737
