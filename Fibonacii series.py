Amount = int(input("Enter the amount of fibonacii series needed "))

n1=0 
n2 =1
count = 0

if Amount <= 0:
   print("Please enter a positive integer")
elif Amount == 1:
   print("Fibonacci sequence upto",Amount,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < Amount:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count = count+1