Dataset Name:	Victorian Road Crash Data
Dataset URL:	https://opendata.transport.vic.gov.au/dataset/victoria-road-crash-data/resource/5df1f373-0c90-48f5-80e1-7b2a35507134
Row Count:	200,352
File Size:	67MB
    
High-Cardinality Column:	ACCIDENT NO
    
Business Case:	The main question I would like to answer using this dataset is: "How do time of day, weather conditions, road surface conditions, vehicle characteristics and location influence the severity of road crashes in Victoria?" The analysis can combine tables also available on the Transport Victoria website which gives further details on the people involved in the accidents, details about the vehicles involved, and the road conditions at the time of the accident. The findings from the data can potentially identify high-risk conditions which make accidents more likely to happen in locations, or between vehicle types in particular road conditions or time of day.

Dataset Justification:	The dataset is large, at approx. 200k records, and contains information about accidents, vehicles, the number of people involved, locations, time of accident, etc. Also, additional information can be sourced from tables such as 'Person', or 'Vehicle' which are available on the Transport Victoria site, meaning that joins will be necessary to answer questions surrounding the business case. Temporal analysis can be done using the date and time of which accidents occurred, and categorical variables such as light conditions can be incorporated to see if there are meaningful associations between those variables and the likelihood/severity of accidents. Also, since the data is large, it can be partitioned by variables to investigate and observe data querying performance which cannot be as easily done by simpler types of filtering or aggregation.

Potential Column Use for A2: 	Potentially useful columns for Assessment 2 include ACCIDENT_DATE and ACCIDENT_TIME for temporal features, SPEED_ZONE and ROAD_GEOMETRY for environmental conditions, BICYCLIST and other vehicle characteristics, and LGA_NAME for location. Numerical variables such as TOTAL_PERSONS, INJ_OR_FATAL, and FATALITY may also be useful, depending on the question that is to be answered and the corresponding target variable selected.
