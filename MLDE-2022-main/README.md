# MLDE-2022

Welcome! This is the repository for MLDE-2022

## The group is arranged as follows

JIAHAO SHANG(2087608)  
XINAN LI(2090506)  
RUIXIN HU(2135790)  
ZIMING GUO(2127468)  
YUNPENG LU(2014873)  
CRYSTAL CAO(2017442)  
JIANGMIAO XIAO(2111422)  

## Conclusion
We generate the wordcloud obtained from analysing reviews:

![wordcloud](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/wordcloud_IMA.png)


After analysing the frequence of different words in reviews, the team chose **four feature** values as follows.
1. Shipping cost ratio -> (payment value-item price)/order price
2. Difference between estimated time to real delivered -> Order estimated delivery date - Order delivered carrier date
3. Product description length -> Assume that the length of the product description has an impact on the product information
4. Product photo qty -> Assume that the number of product images has an impact on the product information

The team divided the Y values into two cases.
The first: a group of 1-3 customer ratings, a group of 4, a group of 5, a total of three classes
The second: a group of customers with ratings below 4, a group of customers with ratings above or equal to 4, a total of two classes

Predictive models(Results may vary depending on each optimization! )
A total of **five algorithms** were used in this study: support vector machines, decision trees, logistic regression, random forests and deep learning algorithms.

For **two classes**, the best result is **Random Forest** and f1-score = 0.8890688259109312.  
For **three classes**, the best result is **Random Forest** and f1-score = 0.4312991351436101.  


The f1-score of every algorithm is shown below:

For **2 classes classification** problem

![Binary-Classification-result](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/Binary%20Classification.png)

For **3 classes classification** problem

![3_Class-Classification-result](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/3_class%20Classification.png) 

## Description of data files/Documentaion

We have built many files:

* [raw data](https://github.com/Lynn-Luyp/MLDE-2022/tree/main/raw%20data): The orginal data downloaded from moodle
* [wordcloud_IMA](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/wordcloud_IMA.png): In order to select the best(most weighted) feastures from all features, we generate a wordcloud to help us to find the best suitable words from reviews. In our opinions, if consumers write "delievery is good" with 5 stars or write "delivery is bad" with 1 star in the review, it is clear that delievery is literally essential to decide the review is one-star or five-stars, which means that the word "delievery" is very important. We can calculate the frequency of occurrence of different words and generate a wordcloud to visualise the outcome.
* [brain map](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/brain%20map.png): Mind map after discussion
* [Pre-processed data](https://github.com/Lynn-Luyp/MLDE-2022/tree/main/Pre-processed%20data): The preprocessed csv files 
* [Binary-Classification-result](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/Binary%20Classification.png): The f1-score of every algorithm when doing binary classication(The samples have 2 labels: good(4* and 5*) and bad(below 4*))
* [3_Class-Classification-result](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/3_class%20Classification.png): The f1-score of every algorithm when doing 3_class classication(The samples have 3 labels: 5*, 4* and bad(below 4*))
* [Notebook with full implementation](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/MLDE%20IMA.ipynb): The notebook contains all details in the project
* [Project description](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/Project%20description.docx): The detailed description and conclusion of this project 
* [training and prediction](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/Model%20training%20and%20Prediction%20script.ipynb): The best model and its prediction, which used the random forest algorithm
* [nn_utils.py](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/nn_utils.py): a ultis file contains all the functions used in Neural Network Algorithm

## Data engineering scripts

* [raw data](https://github.com/Lynn-Luyp/MLDE-2022/tree/main/raw%20data): The orginal data downloaded from moodle
* [Pre-processed data](https://github.com/Lynn-Luyp/MLDE-2022/tree/main/Pre-processed%20data): The preprocessed csv files 

## Model training and Prediction script
* [training and prediction](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/Model%20training%20and%20Prediction%20script.ipynb): The best model and its prediction, which used the random forest algorithm

## Notebook contains the full implementation

* [Notebook with full implementation](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/MLDE%20IMA.ipynb): The notebook contains all details in the project

## Project description

* [Project description](https://github.com/Lynn-Luyp/MLDE-2022/blob/main/Project%20description.docx): The detailed description and conclusion of this project 








