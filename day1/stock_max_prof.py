class Solution(object):
    def maxProfit(self, prices):
        min = 696969
        p=0
        for a in prices:
          if min>a:
            min=a
          elif p<a-min:
            p=a-min
        return p
          
