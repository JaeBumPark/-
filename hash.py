# Hash_dict = {}

# A=["min", "bum", "hwang"]

# for i in A:
#     Hash_dict[hash(i)] = i
#     # Hash_dict[i] = hash(i)

# # min_hash = hash("min")
# # min_string = Hash_dict[min_hash]
# # print("Hash Value of 'min':", min_hash)
# # print("String associated with Hash Value:", min_string)
# print(Hash_dict)

B= ["FD", "FF", "FDf"]
B_keyvaluelist= []
for key,value in enumerate(B):
    B_keyvaluelist.append({key,value})
    
print(B_keyvaluelist)    