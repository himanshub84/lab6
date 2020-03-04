#Q1:-
a={"band":"ford","model":"mustang","year":1964}
print(a)

#Q2
b=1964
for key,value in a.items():
    if b==value :
        print(key)


#Q3
a["model"]="ecosport"
#Q4
a["brand"]="m001"
a["colour"]="RED"
print(a)

#Q5
for i in a :
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
#Q6
if a["model"]=="ecosport":
    print("Exist")

#Q7
a.pop("brand")

#Q8
c=a.copy()
d=dict(a)
