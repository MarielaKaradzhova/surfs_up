# Surf's Up 
*Investing in Waves and Ice Cream*

![](https://github.com/MarielaKaradzhova/surfs_up/blob/main/Resources/surf_shop.png)

*Surf and Ice Cream shop on the beautiful island of Oahu,Hawaii*
## Purpose of Project
The purpose of this project is to explore and analyze weather data in order to determine if it would be a good investment to start a surf and ice cream shop in Oahu, Hawaii.



## Overview of Statistical Analysis
### Resources
Data Source: hawaii.sqlite

Software: Python 3.7.6, Visual Studio Code, 1.52.1, Jupyter Notebook 6.1.4

Link to the full code here: https://github.com/MarielaKaradzhova/surfs_up/blob/main/SurfsUp_Challenge.ipynb
### Analysis Summary
This analysis was performed using SQLAlchemy, a query tool for SQLite, used w. This tool integrates statistical analysis with dataframe analysis, making it possible to retrieve weather data from the dataset <hawaii.sqlite> found in the "Resources Folder" of this repository. The goal of this analysis was to obtain summary statistics of temperatures in the months of June and December from the weather database.

### Results
Below is a **bulleted list** which describes the three key differences in weather between June and December from all counts:

- First, the average temperature for December is 71°F, where in July the average temperature is 74°F. That is an average of 3°F higher in June compared to December.
- Second, the lowest temperature in December is equal to 56°F, in comparison to 64°F in July. There is a bigger difference of 8°F between the two months.
- Third, the highest temperature is 83°F for December and 85°F for June. Important to note that this is the smallest difference between December and June, only 2°F.


**Temperature Summary Statistics for June and December from Query Results**


![](https://github.com/MarielaKaradzhova/surfs_up/blob/main/Resources/june_summary.png)|![](https://github.com/MarielaKaradzhova/surfs_up/blob/main/Resources/december_summary.png)


#### Additional Queries to Perform 
To deepen the analysis of this project, it is important to gather more data and the best way to do this is by creating additional queries. One possible query could be to look at the rainfall for the 75th percentile for December and June. 
Second, it would be useful to look at the temperatures and levels of precipitation, in relation to the elevation and time of observation to determine if there is any difference in the elevation or time of observation when there is more or less rain, and how that can have an effect on the temperatures in the months of June and December.
