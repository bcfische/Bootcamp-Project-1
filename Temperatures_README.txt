Temperature data is collected from "https://www.ncdc.noaa.gov/cdo-web/datatools/lcd"

User can query by "Location Type" = County, which then requires user to select State and County

I then selected one representative City from the list, one with the most available data 

Queries are limited by file size (9 years or so seems to be the max), so to get 2004-2018 requires two separate queries

"GetTemps.ipynb" reads in two csv files and combines them into one csv containing hourly temperatures (roughly 24 per
day per year) -> <City_HourlyTemps.csv>

"getmax.py" uses the output of "GetTemps.ipynb" to find the daily maximum temperature (one per day per year). It also
maps the city name to county name when writing the output file -> <County_MaxTemps.csv>

"SortByYear.ipynb" uses the output(s) of "getmax.py" and creates a csv with rows for each day and columns for each year.
It also calculates the daily average -> <County_Yearly.csv>
