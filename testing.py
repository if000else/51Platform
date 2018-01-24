import hashlib
md5 = hashlib.md5('123456'.encode())
a = md5.hexdigest()
print(a,len(a))
