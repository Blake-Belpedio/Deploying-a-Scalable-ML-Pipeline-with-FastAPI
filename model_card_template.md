# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a random forest classifier with no hyperparmeter tuning.

## Intended Use
This model is used to predict wether or not a persons income is above or below $50,000 based on various demographic and employment parameters.

## Training Data
The training data used comes from the UC Irvine Machine learning repository and can be found at this link.
Link: https://archive.ics.uci.edu/dataset/20/census+income
Citation data: Kohavi,Ron. (1996). Census Income. UCI Machine Learning Repository. https://doi.org/10.24432/C5GP7S.

When preprocessing this data OneHotEncoder() was used to handle missing data. A baisc Split/Tain/Test was utilized where 20% of the data was witheld for testing and validation, while 80% was used to train the model. 

## Evaluation Data
The evaluation was performed on 20% of the orignal data set.

## Metrics
The metrics choosen for this model are displayed with their respective results below:
Precision: 0.7419
Recall: 0.6384
F1: 0.6863
## Ethical Considerations
As always Human error and biases should be considered in the collection of the data and how those biases will impact our model. This may lead to an inaccurate model.

## Caveats and Recommendations
The data used comes from the 1994 census. At the time of this project 30 years have elapsed and the data is likely to no longer give an accurate portrayl of reality. It is therefore reccomended that no changes be made on accound of this analysis. This analysis could be useful in comparison with subsequent censuses to view changing trends among salary in groups. Errors should be accounted for in both the collection and storage of the data.