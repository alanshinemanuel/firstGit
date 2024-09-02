def factorial():
  if type(n)!=int:
    return -1
  else if n<0:
    return -1
  else if n==0:
    return 1
  else:
    return n*factorial(n-1)
n=int(input("enter number"))
