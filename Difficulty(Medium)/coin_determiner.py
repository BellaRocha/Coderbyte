#Coin Determiner

#Have the function CoinDeterminer(num) take the input, which will be an integer ranging from 1 to 250, and return an integer output that will specify the least number of coins, that when added, equal the input integer. Coins are based on a system as follows: there are coins representing the integers 1, 5, 7, 9, and 11. So for example: if num is 16, then the output should be 2 because you can achieve the number 16 with the coins 9 and 7. If num is 25, then the output should be 3 because you can achieve 25 with either 11, 9, and 5 coins or with 9, 9, and 7 coins.

#Examples:
#Input: 6 
#Output: 2
#Input: 16 
#Output: 2

#Tags:
#Amazon
#Math Fundamentals
#Optimization

#Python:
import itertools
def CoinDeterminer(num): 
  coins = [1, 5, 7, 9, 11]
  
  count_coins = 0
  
  while True:
    count_coins += 1
    for c in itertools.combinations_with_replacement(coins, count_coins):
      if sum(c) == int(num):
        return count_coins

    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print CoinDeterminer(raw_input())
