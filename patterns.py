# # pyramid
# for i in range(5):
#     for j in range(5-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1 ):
#         print("*", end=" ")
#     print(" ")

# # pyramid
# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(2*i-1 ):
#         print("*", end=" ")
    
    
#     print(" ")





# for i in range(1,6):
#     # print(i)
#     for j in range(1,i):
#         print(j,end=" ")
#     print("")
# for i in range(1,6):
#     # print(i)
#     for j in range(1,i):
#         print(i,end=" ")
#     print("")

# n=5

# for i in range(n):
#     for j in range(n,i,-1):
#         print("*",end="")
#     print(" ")
# n=5

# for i in range(n):
#     for j in range(i,n):
#         print(j,end="")
#     print(" ")

# n = 5

# for i in range(2 * n):
#     if (i <= n + 1 // 2):
#         for j in range(i):
#             print("*", end ="")
#     else:
#         for j in range(2 * n - i):
#             print("*", end ="")
#     print(" ")


# n=5

# start=0
 
# for i in range(n):
#     if(i%2 !=0):
#        start =1
#     else:
#         start=0
#     for i in range(i):
#         print(start, end =" ")
#         start = 1-start

#     print(" ")


# n=5
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(j , end="")
#     for j in range(n,i+1,-1):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j, end="")
  
#     print(" ")

# n=5
# s=1
# for i in range(n):
#     for j in range(i):
#         print(s,end=" ")
#         s+=1
#     print(" ")

# n=5
# for i in range(n):
#     for j in range(i):
#         print(chr(97+j), end=" ")

#     print("")
# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print(chr(97+i), end=" ")
#     print("")

# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for j in range(2*i+1):
#         print(chr(97+i), end=" ")
#     print(" ")


n=10

for i in range(n,0,-1):
    if(i<(n+1)//2):
        for j in range(i,0,-1):
            print("*",end ="")
        for j in range(i):
            print(" ",end ="")
        # for j in range(i):
        #     print(" ",end ="")
        # for j in range(n,i,-1):
        #     print("*",end ="")

    # else:
    #     for j in range(1,n-i):
    #         print("*",end ="")
    #     for j in range(i):
    #         print(" ",end ="")
        # for j in range(i):
        #     print(" ",end ="")
        # for j in range(n,i,-1):
        #     print("*",end ="")

    
   
   
    print(" ")

