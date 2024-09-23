# n=123

# rev=0
# for i in range(3):
#     print(n%10)
#     rev=rev*10+n%10
#     n//=10
#     print(rev)


# print(rev)


# print(min(1,2))


a,b=12,28

# result = min(a, b)

# while result:
#     if a % result == 0 and b % result == 0:
#         break
#     result -= 1

# print(result)

# while b:
#     a, b = b, a % b

# print(a)

# while a :

#     # print(b)
#     # print(a%b)
#     b=a
#     a=b%a

  
# while b:

#     # print(b,a)



#     a=b  
#     b=a%b
  


# # print(12%10)
# # print(10%2)

# # print(b)

# print(a)

gcd=0
for i in range(2,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i


print(gcd)


while (a>0 and b>0):
    if (a>b):
        a=a-b
    else:
        b=b-a

if(a==0):
    print(b)
else:
    print(a)


 






