# Surfs Up
 Advanced Data Storage and Retrieval.

## Overview of the analysis: 
Explain the purpose of this analysis.

## Background
Upon a trip to Oahu, Hawaii, we fall in love with the place and decide to move there. In a meeting with W. Avy, a very successful surfer, we understand he needs to be cognisant of the weather conditions if he plans to be successful in in his second attempt to open a sports shop there. So after the first meeting, we create a weather analysis to share with him and ask his opinion.

W. Avy likes our analysis, but he wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

### What We Are Creating
We have been tasked to create two technical analysis deliverables and a written report:

 1: Determine the Summary Statistics for June
 2: Determine the Summary Statistics for December
 3: A written report for the statistical analysis (README.md)


## Methods: 
In this analysis we used SQLite to store the weather data that W. Avy shared with us and that we used for our analysis. In order to connect to the SQLite database, we employed SQLAlchemy. SQLAlchemy helped us easily connect to our database where we were planning to store the weather data.

We also used Python, Pandas functions and methods, and SQLAlchemy for the analysis. We filtered the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of June and December. We then converted those temperatures to a list, createed a DataFrame from the list, and generated a summary statistics table for each month.


## Results:
The results of the analysis showed that the average temperature between the months of June and December were nearly the same (74.9°F vs 71°F, respectively) as were the maximum temperatres between the two months (86°F vs 83°F), Figure 1.


Figure 1: Comparative analysis of temperature between the months of June and December.

-------------------
![3-comparative-temp.png](https://github.com/BHashemi2021/surfs_up/blob/main/Resources/3-comparative-temp.png)

-------------------

There is a bulleted list that addresses the three key differences in weather between June and December. 

Use images as support where needed.

## Summary: 

There is a high-level summary of the results and 

$$$$ there are two additional queries to perform to gather more weather data for June and December.



Figure 2: Comparative analysis of precipitations between the months of June and December.

-----------------------
![3-comparative-percip.png](https://github.com/BHashemi2021/surfs_up/blob/main/Resources/3-comparative-percip.png)

-----------------------



Figure :
![]()

