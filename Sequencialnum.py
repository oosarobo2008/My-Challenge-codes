
# Question : The included code stub will read an integer n without using any string methods,
#  try to print the following: 1,2,3,4,...,n
#Note that "..." represents the consecutive values in between.

a = int(input('Enter start number:'))
b =  int(input('Enter end number'))
for n in range(a, b + 1):
     # checking condition
    if n >= 0:
      print (n , end = " ") 