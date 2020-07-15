# airbnb-data-modeling
## Libraries:
numpy, pandas, lightgbm, matplotlib, scikit learn, scipy, warnings
## Data
Data can be found at https://www.kaggle.com/airbnb/seattle files calendar.csv, listings_seattle.csv
## Introduction
Airbnb day prices in Seattle are predicted using feature engineering, random forest and light gradient boosting feature selection and regression. These models aim to help hosts establish appropriate rental prices and also to find out what features can influence rental price the most. Text features such as name and description are also considered. 
Here we also compare random forest and light gradient boosting performance. Light Gradient Boosting (LGB) is relatively fast algorithm comparing with other boosting methods. In the final test the sum of two LGB models was applied to reduce overfitting. 
## Files
files: airbnb.pynb - code; listings_seattle.csv - data (calendar.csv does not fit to my github, go to https://www.kaggle.com/airbnb/seattle)
## Author:
Inga Kuznetsova
## Results
In https://www.kaggle.com/aleksandradeis/airbnb-seattle-reservation-prices-analysis was used RF, price dependence on month and 'month' feature. Division on test and train was different and resulted to the same id in test and train and overfitting.  Other features selection is different.

The Airbnb rent prices noticeably depend on month of the year. The highest prices are in the summer. 
The other features that are influence prices the most are total number of rooms, month, latitude, longitude, accommodates (total number of people to accommodate), room type, reviews per month, host total listening counts, street.
The light gradient boosting model has better prediction score than Random forest for our most optimal feature selection. In the Light Gradient Boosting Regression features importance weights are distributed more homogeneously. 
Property description can also give information about price. 
Combining two models with less number of features can improve resulting test score. Final test R-squared score is 0.737
