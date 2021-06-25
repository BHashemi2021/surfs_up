# Surfs Up
##### Advanced Data Storage and Retrieval.
--------------------------
![Surfing-boards.png](https://github.com/BHashemi2021/surfs_up/blob/main/Resources/Surfing-boards.png)

--------------------------
 

## Overview of the analysis: 
Explain the purpose of this analysis.

## Background
Upon a trip to Oahu, Hawaii, we fall in love with the place and decide to move there. In a meeting with W. Avy, a very successful surfer, we understand he needs to be cognisant of the weather conditions if he plans to be successful in in his second attempt to open a sports shop there. After the first meeting, we created a weather analysis to share with him.

W. Avy likes our analysis, but he wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

### What We Are Creating
We have been tasked to create two technical analysis deliverables and a written report:

 1: Determine the Summary Statistics for June
 2: Determine the Summary Statistics for December
 3: A written report for the statistical analysis (README.md)


## Methods: 
In this analysis we used SQLite to store the weather data that W. Avy shared with us and that we used for our analysis. In order to connect to the SQLite database, we employed SQLAlchemy. SQLAlchemy helped us easily connect to our database where we were planning to store the weather data.

We also used Python, Pandas functions and methods, and SQLAlchemy for the analysis. We filtered the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of June and December. We then converted those temperatures to a list, created a DataFrame from the list, and generated a summary statistics table for each month.


## Results:
 1- The results of the analysis showed that the average temperature between the months of June and December were nearly the same (74.9 °F vs 71 °F, respectively). 
 
 2- The maximum temperatures between the two months of June and December were nearly the same too (86 °F vs 83 °F), Figure 1.

 3- On the other hand the minimum temperatures were rather different between the two months of June and December (64 °F vs 56 °F), Figure 1.
 
 
 
##### Figure 1: Comparative analysis of temperature between the months of June and December.

-------------------
![3-comparative-temp.png](https://github.com/BHashemi2021/surfs_up/blob/main/Resources/3-comparative-temp.png)

-------------------

To better compare the two months and verify the two months were pleasant enough for surfing as well as going for an ice-cream, two more queries were performed on the SQLite database. We compared the precipitations in the two months as follows:

#### 1. Extra query to calculate the amount of percepitations in June

```ruby
results = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()
df = pd.DataFrame(results, columns=['date','precipitation'])
df.set_index(df['date'], inplace=True)
df.describe()
``` 

#### 2. Extra query to calculate the amount of percepitations in December

```ruby
results = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 12).all()
df = pd.DataFrame(results, columns=['date','precipitation'])
df.set_index(df['date'], inplace=True)
df.describe()
```

The results from the comparative analysis of precipitations between the month of June and December showed that:
 
 1-  There is a roughly two-fold rainfall in December versus June  (Figure 2)
 
 2- The maximum amount of rainfall seems t be 2 inches more in December compared to June (Figure 2)


##### Figure 2: Comparative analysis of precipitations between the months of June and December.

-----------------------
![3-comparative-percip.png](https://github.com/BHashemi2021/surfs_up/blob/main/Resources/3-comparative-percip.png)


## Summary: 

All in all, the average temperatures between the months of June and December are good enough to go surfing or for an ice-cream or both. Nevertheless, the rainfalls seem to be rather higher in December. The prospects for opening a surf shop seems to be relevant in June but eating ice-cream on a rainy December day needs a rather different taste but not that rare.




----------------------------------------------------------------------------------
Hawaii is popular tourist destination all year round nearly 750 miles of coastline, diverse landscape in the middle of a backdrop of mountains, warm tropical climate, and abundant public beaches. The best time to visit Hawaii is from May to October in the dry season, particularly in May and June, as the summer temperatures are not extreme. There is regular threat of thunderstorms and hurricanes (mostly non-destrucive) from July to December (1).


#### References:
1- Monthly weather forecast and climate Hawaii, USA, accessed June 25, 2021 at: https://www.weather-us.com/en/hawaii-usa-climate
