def operatorOr(a, b):
   c=a+b
   c.sort()
   return c

#AND operator
# a = [1, 3, 5, 8, 9]
# b = [3, 4, 7, 9, 10]
# c = [3, 9]
def operatorAnd(a,b):
   p1 = 0
   p2 = 0
   c = list()
   while p1 < len(a) and p2 < len(b):
      if a[p1] == b[p2]:
         c.append(a[p1])
         p1 += 1
         p2 += 1
      elif a[p1] > b[p2]:
         p2 += 1
      else:
         p1 += 1
   return c

def operatorNot(a,b):
   return 1
