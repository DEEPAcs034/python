num=input('enter a value:')
if num==num[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
for i in range(10):
    if num.count(str(i))>0:
        print(f'{str(i)}appears{num.count(str(i))}times')
