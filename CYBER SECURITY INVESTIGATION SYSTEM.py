print("========CYBER SECURITY INVESTIGATION SYSTEM=========")
name=input("Agent Name:")
age=int(input("Age:"))
pas=input("Password:")
scl=input("Secret Letter:")
sn=int(input("Security Number:"))

print("=====Name Analysis=====")
print(name[0])
print(name[-1])
print(len(name))

if len(name)<5:
    print("Short Codename")
elif len(name)>=5 and len(name)<=8:
    print("Standard Codename")
else:
    print("Long Codename")
scl_found=False
for ch in name:
    if ch==scl:
        print("Match Found")
        scl_found=True
if scl_found:
    print("Total Matches:",name.count(scl))
print("PASSWORD SECURITY CHECK")
if len(pas)<4:
    print("Weak")
elif len(pas)>=4 and len(pas)<=7:
    print("Medium")
elif len(pas)>=8:
    print("Strong")

if len(pas)>1:
    print(pas[1])
print(pas[-1])

x=5

while x>0:
    print(x)
    x-=1
    if x==0:
        print("Investigation Started")

print(name[0:3])
print(name[-2:])

if sn%2==0:
    print("Even Security Code")
else:
    print("Odd Security Code")

if age>=13 and age<=19 and scl_found and len(pas)>=8 and sn%2==0:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

print('======= FINAL REPORT =======')

print("Agent:",name)
print("Age:",age)
print("Name Length:",len(name))
if scl_found:
    print("Secret Matches:",name.count(scl))
else:
    print("Secret Matches:0")
if len(pas)<4:
    print("Password Status: Weak")
elif len(pas)>=4 and len(pas)<=7:
    print("Password Status: Medium")
elif len(pas)>=8:
    print("Password Status: Strong")
if sn%2==0:
    print("Security Code: Even")
else:
    print("Security Code: Odd")

if age>=13 and age<=19 and scl_found and len(pas)>=8 and sn%2==0:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")


    
