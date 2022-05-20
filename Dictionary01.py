a = {}
size = int(input("Enter the size of dict : "))
for i in range(0,size):
    key = input("Enter the keys of dict : ")
    value = int(input("Enter the value of dict : "))
    a.update({key:value})
print(a)