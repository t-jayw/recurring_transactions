import sys
from datetime import datetime

import pandas as pd

MINT_DATE_FORMAT = "%m/%d/%Y"
MINT_MERCH_COLUMN = "Description"
MINT_DATE_COLUMN = "Date"
MINT_AMT_COLUMN = "Amount"


def parse_date(datestring, format):
  return datetime.strptime(datestring,  format)


def calculate_date_diff(list):
  diffs = []
  for i in range(0,len(list)-1):
    diffs.append(diff_month(parse_date(list[i], MINT_DATE_FORMAT), 
    parse_date(list[i+1], MINT_DATE_FORMAT)))
  return diffs


def diff_month(d1, d2):
  return(d1.year - d2.year)*12 + d1.month - d2.month


def unique_merchants(df, merch_column = MINT_MERCH_COLUMN):
  return df[merch_column].unique().tolist()


def merchant_price_txn_list(df, merchant_name,  txn_amount,
                      merch_column = MINT_MERCH_COLUMN, date_column = MINT_DATE_COLUMN,
                      amt_column = MINT_AMT_COLUMN):
  return df[(df[merch_column] == merchant_name) & (df[amt_column] == txn_amount)][date_column].tolist()


def unique_pricepoints(df, merchant_name, 
                      merch_column = MINT_MERCH_COLUMN, amt_column = MINT_AMT_COLUMN):
    return df[(df[merch_column] == merchant_name)][amt_column].unique().tolist()


def main(csv):
  foo = pd.read_csv(csv)
  print("reading csv")
  print("Read rows:", len(foo.index))
  for merch in unique_merchants(foo):
    for pricepoint in unique_pricepoints(foo, merch):
      unique_mo_diffs = set(calculate_date_diff(
                         merchant_price_txn_list(foo, merch, pricepoint)))
      if len(merchant_price_txn_list(foo, merch, pricepoint)) < 3:
        pass
      elif unique_mo_diffs != {1}:
        pass
      else:
        date_list = merchant_price_txn_list(foo, merch, pricepoint)
        print merch, "\n", "$", pricepoint, "\n", date_list, "\n"

if __name__ == '__main__':
  txn_csv = sys.argv[1]
  main(txn_csv)
