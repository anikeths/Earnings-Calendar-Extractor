# Earnings-Calendar-Extractor
This code written in Pyhton gets the earnings calendar of companies in Python dictionary format.


Earnings Conferencd Calls are very important events for companies.
Financial analysts keep a sharp eye on the trends before and after an earnings call has taken place - especially the stock reurn fluctuations.

This code aims to 
1)extract earnings dates sourced from publicly available datasets.
2)A database of daily stock return is downloaded from the CRSP database provided by the Wharton Research Data Services.
3)The code goes through the date column in the calendar
4)A new column in the table is created that logs 1 for match with the date column of the earnings date and 0 for a non-match.

