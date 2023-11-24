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

as_ci = []
for i in list_1:
    sum = 0
    for j in i:
        asci = ord(j)
        sum = sum+asci
    as_ci.append(asci)
print(as_ci)