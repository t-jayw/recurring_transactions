# recurring_transactions
looks for monthly recurring transactions in csv of transactions

usage: python transactions.py <your csv file>

It's set up to work nicely with data from mint.com. You can go to you transactions page on mint and at the bottom select "Download all <x> transactions" and use that CSV directly with this program. CSVs from other sources could still work, you'd just need to adjust the column names in the program to whatever your columns are, and the date format if it's different. 

My first run found $39 in redundant or unwanted monthly subscriptions, and $69 of monthly subscriptions that I realized could be expensed through a fitness reimbursement program. Great success! 

Sample output: http://i.imgur.com/ICvzfoU.png
