# recurring_transactions
looks for monthly recurring transactions in csv of transactions that have ocurred at least thrice

usage: python transactions.py *your csv file* 

example:
> python transactions.py /Users/tyler/Downloads/transactions.csv

(If on a mac, probably '/Users/_yourusername_/Downloads/transactions.csv')

It's set up to work nicely with data from mint.com. You can go to you transactions page on mint and at the bottom select "Download all <x> transactions" and use that CSV directly with this program. CSVs from other sources could still work, you'd just need to adjust the column names in the program to whatever your columns are, and the date format if it's different. 

One 'gotcha' -- you need to have the pandas python package installed, instructions on how to do that here:
http://pandas.pydata.org/pandas-docs/stable/install.html

My first run found $39 in redundant or unwanted monthly subscriptions, and $69 of monthly subscriptions that I realized could be expensed through a fitness reimbursement program. Great success! 

Sample output: http://i.imgur.com/ICvzfoU.png
