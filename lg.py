# product_info = ["1 2 5","1 3","2 4 6"]
# custom_info = ["1 2 5 6","2 3 4","1 3 4"]
# k = 2
# def solution(k,product_info,custom_info):
#     answer = []
#     products , customs = [],[]
#     for prod in product_info:
#         products.append(list(map(int,prod.split())))
#     for cust in custom_info:
#         customs.append(list(map(int,cust.split())))
#     return customs        

# print(solution(k,product_info,custom_info))

custom_info = ["1 2 5 6","2 3 4","1 3 4"]

for cust in custom_info:
    # customs.append(list(map(int,cust.split())))
    print(cust)