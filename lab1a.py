a=int(input('marks for test1:'))
b=int(input('marks for test2:'))
c=int(input('marks for test3:'))
best_of_two=sorted([a,b,c],reverse=True)[:2]
average=sum(best_of_two)/2
print("Average :",average)