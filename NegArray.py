def negative (temperature):
   days = 0
   for t in temperature:
    if t < 4:
      days += 1
   return days
temperature = [1,2,3,4,5,6,7,8,9,10]
(days) = negative(temperature)
print(days)