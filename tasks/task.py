import re
i=input("enter string")
pattern="^[a-zA-Z_][a-zA-Z_0-9]*$"
res=re.search(pattern,i)
if res:
    print("valid identifier")
else:
    print("invalid identifier")

import re
i=input("enter string")
pattern="^[a-zA-Z_][a-zA-Z_0-9]*$"
words=i.split()
valid_identifiers=[w for w in words if re.match(pattern,i)]
print(valid_identifiers)

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
s=a+b+c
print(f"sum is {s}")

