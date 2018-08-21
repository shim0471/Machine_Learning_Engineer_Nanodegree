# Machine Learning Engineer Nanodegree

# Capstone Project

# Home Credit Default Risk


## Table of Contents  
- [Project Overview](#project-overview)
- [Project Highlights](#project-highlights)
- [Install](#install)
- [Files](#file)
- [Code](#code)



### <a name="project-overview"></a>Project Overview

Many people struggle to get loans due to insufficient or non-existent credit histories. And, unfortunately,
this population is often taken advantage of by untrustworthy lenders.
While Home Credit is currently using various statistical and machine learning methods to make these predictions,
they're challenging Kagglers to help them unlock the full potential of their data.
Doing so will ensure that clients capable of repayment are not rejected and that loans are given with a principal, maturity,
and repayment calendar that will empower their clients to be successful.

### <a name="project-highlights"></a>Project Highlights

This project is an attempt to solving the [Home credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk)

- How to load large datasets from multiple files in different directories.
- Processed and cleaned real-world data.
- Built a classification model with LigntGBM and XGBoost that ranked top 20% on a leaderboard of 1500+.
- For Feature Selection, I used a open source library 'FeatureSelector' class by WillKoehrsen

### <a name="install"></a>Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [Jupyter Notebook](http://jupyter.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [LightGBM](https://lightgbm.readthedocs.io/en/latest/)
- [XGBoost](https://xgboost.readthedocs.io/en/latest/)
- [FeatureSelector](https://github.com/WillKoehrsen/feature-selector)


### <a name="file"></a>Files

This Capstone folder include:
- dataset with original datasets and merged datasets. This files was merged with all dataset after feature Selection.
  but now is empty because it is pretty big.
- proposal.pdf
- report.pdf
- Ipython folder
- Html folder
- FeatureSelector class



### <a name="code"></a>Code

Data Processing codes are provided in the Jupyter notebook `Ipython/Capstone_part01.ipynb`, `Ipython/Capstone_part02.ipynb`,
`Ipython/Capstone_part03.ipynb`. And HTML files in `Html` folder.
