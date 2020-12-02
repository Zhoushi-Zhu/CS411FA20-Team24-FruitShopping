import requests
import sys

argc = len(sys.argv)
if argc == 1:
    print("Expected Usage: PurchaseDate, Quantity, EmailAccount, ProductID , StoreID")

arg_list = [str(x) for x in sys.argv]
print(arg_list[2])
url = 'http://localhost:3000/post-test-xml'
myobj = {'PurchaseDate': arg_list[1], 'Quantity':arg_list[2], 'EmailAccount':arg_list[3], 'ProductID': arg_list[4],'StoreID': arg_list[5]}

x = requests.post(url, data = myobj)

print("***************User Create Results******************")
print(str(x.text))
# print("****************Current User Table******************")
#
# url = 'http://localhost:3000/purchases'
#
# x = requests.get(url)
#
# print(str(x.text))

# url = 'http://localhost:3000/customers/zzhu31@illinois.edu'
# myobj = {'email': 'random@illinois.edu', 'name':'random', 'active':0}
# x = requests.put(url, data=myobj)
#
# print("update results:",x.text)
# print(type(x.text))
