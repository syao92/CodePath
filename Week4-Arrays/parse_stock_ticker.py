#Given a string representing a stock ticker:

# Input: "AAPL 313 GOOG 513 TSLA 58 BBY 22"
# Output: "AAPL 313 BBY 22 GOOG 513 TSLA 58"


# Write a function that returns the stocks alphabetized

# Differentiate stocks
# 1a) If not between A - Z return 0
# 1b) Split on space
  # [AAPL,313,BBY,22,GOOG,513,TSLA,58]
  # Stock Name, Stock Value
  # i = 0, AAPL i + 1 => 313
# 2) Iterate through and combine stock name and value
  # Can Use join
  # curr_string => AAPL 313
  # new_arr => [AAPL 313,GOOG 513,TSLA 58,BBY 22]
# 3) Sort

def alphabetical_stocks(str):
  stock = str.split(" ")
  concat_stock = []
  print(stock)

  for i in range(0, len(stock), 2):
    concat_stock.append(stock[i] + ' ' + stock[i+1])
  concat_stock.sort()
  print (concat_stock)

alphabetical_stocks("AAPL 313 GOOG 513 TSLA 58 BBY 22")

## Stretch

# Write a function that returns the cheapest priced stock symbol

test_1 = "AAPL 313 GOOG 513 TSLA 58 BBY 22" # BBY
test_2 = "NBA 12 AAPL 313 GOOG 513 TSLA 58 BBY 222" #NBA
test_3 = "NBA 11 AAPL 55 GOOG 22 TSLA 44 BBY 22" # NBA


def cheapest_stock(str):
  # Variables to hold cheapest stock name and value
  cheapest_stock_value = 0
  cheapest_stock_name = ""
  split_arr = str.split(" ")

  # Checks current cheapest_stock_value. If its the first stock_value
  # or if the current stock_value is cheaper than cheapest
  # set the new cheapest_stock_value and cheapest_stock_name
  for index in range(1, len(split_arr), 2):
    if (index == 1 or int(split_arr[index]) < cheapest_stock_value):
      cheapest_stock_value = int(split_arr[index])
      cheapest_stock_name = split_arr[index - 1]

  print(cheapest_stock_name)
  
# cheapest_stock("AAPL 313 GOOG 513 TSLA 58 BBY 22")
# cheapest_stock("NBA 12 AAPL 313 GOOG 513 TSLA 58 BBY 222")
# cheapest_stock("NBA 11 AAPL 55 GOOG 22 TSLA 44 BBY 22")