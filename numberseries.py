nterms = int(input("How many terms?"))
n1,n2 = 0,1
count = 0
if nterms <= 0:
  print("please enter a positive integer")
elif nterms ==1:
    print("Fibanocci sequence upto",nterms,":")
    print(n)
else:
    print("Fibanocci sequence:")
    while count < nterms:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1
    
