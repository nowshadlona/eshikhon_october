# list_1 = [10,20,30,40,50,60]
# list_2 = ["abcd", "efgh"]

# for i in range(len(list_1)):    
#     print(i,list_1[i])
#     sum = 0
# for i in list_1:
#     sum = sum + i
# print(sum)

# for n in range(len(list_2)):
#     print(n,list_2[n])
# sum = 0
# for n in list_2:
#     sum = sum +len(n)
# print(sum)


list_1 = ['ab', 'cd', 'ef']
list_2 = []
sum = 0

for row in list_1:
    
    for colm in row:
        asci = ord(colm)
        sum = sum+asci
    list_2.append(sum)
print(list_2)