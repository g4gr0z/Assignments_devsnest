class Solution(object):
  def isAnagram(self, sts, tt):
    s = list(sts)
    s.sort()
    t = list(tt)
    t.sort()
    if s==t:
      return True
    else:
      return False
