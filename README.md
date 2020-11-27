# Web-Scrapping using Beautifulsoup
In this project, i will scrape a data from the website https://www.exchange-rates.org/history/IDR/USD/TI, which is about the historical exchange rates between the Indonesian Rupiah (IDR) and the US Dollar (USD). From this data, I will visualize the data with a simple flask dashboard. The data that be visualized is the highest, lowest and average money exchange rates every month (from June, 1st 2020 until November, 25th 2020)

This notebook also contains the steps I took to perform web scrapping using BeautifulSoup and data visualization with flask dashboard. The steps are described below :

1. Requesting the Data and Creating a BeautifulSoup
2. Finding the right key to scrap the data & Extracting the right information
3. Creating data frame & Data wrangling
   a. Put the array into dataframe
   b. Do data cleaning dan data wrangling
   c. First data visualization using matplotlib
   d. Implementing webscrapping to the flask dashboard
4. Analysis and Conclusion

## What is BeautifulSoup?
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

These instructions illustrate all major features of Beautiful Soup 4, with examples. I show you what the library is good for, how it works, how to use it, how to make it do what you want, and what to do when it violates your expectations.

This document covers Beautiful Soup version 4.9.2. The examples in this documentation should work the same way in Python 2.7 and Python 3.8.

You might be looking for the documentation for Beautiful Soup 3. If so, you should know that Beautiful Soup 3 is no longer being developed and that support for it will be dropped on or after December 31, 2020. If you want to learn about the differences between Beautiful Soup 3 and Beautiful Soup 4, see Porting code to BS4.
(https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## What is Web Scrapping
Web scraping is the process of collecting structured web data in an automated fashion. It’s also called web data extraction. Some of the main use cases of web scraping include price monitoring, price intelligence, news monitoring, lead generation and market research among many others.

In general, web data extraction is used by people and businesses who want to make use of the vast amount of publicly available web data to make smarter decisions.

If you’ve ever copy and pasted information from a website, you’ve performed the same function as any web scraper, only on a microscopic, manual scale. Unlike the mundane, mind-numbing process of manually extracting data, web scraping uses intelligent automation to retrieve hundreds, millions, or even billions of data points from the internet’s seemingly endless frontier.
(https://www.scrapinghub.com/what-is-web-scraping/#:~:text=Web%20scraping%20is%20the%20process,market%20research%20among%20many%20others)

# Conclusion
After carrying out several processes and steps as described earlier, 3 results were obtained from data collection, namely the `minimum value,` the `maximum value` and the `average value` for each month. The data was taken from https://www.exchange-rates.org/history/IDR/USD/T from June 1st, 2020 to November 25th, 2020. \

From the coding process using Pyhton and Jupyter Notebook, i get 4 coclusion that i think important.
1. Maximum exchange rate in **September** = IDR 14,892.32
2. Minimum exchange rate in **June** = IDR 13,867.95
3. Highest average exchange rate in **September** = IDR 14,805.98
4. Lowest average exchange rate in **June** = IDR 14,124.30
