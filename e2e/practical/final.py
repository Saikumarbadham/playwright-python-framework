# reverse topics

reverse =1223
cost=0

for res in reversed(str(reverse)):
    cost = int(res) + cost * 10

if cost== reverse:
    print("palindrome")
else:
    print("not palindrome")

#print(cost)

# greater tand and lees than
numbers = [5, 2, 8, 1, 3]

max =float('inf')
smax =float('inf')
ssmax=float('inf')

for num in numbers:
    if num < max:
        smax=max
        max=num
    elif num < smax and max !=num:
        ssmax=smax
        smax=num
    elif num <ssmax and smax !=num and max !=num:
        ssmax=num

print(max)
print(smax)
print(ssmax)

ff = max-smax
print(ff)

#count
numbh="saikumar"
ch ="a"
count =0
for nu in numbh:
    if nu == ch:
        count +=1 
print(count)

# fre
numbh="saikumar"
freq ={}

for kj in numbh:
    if kj in freq:
        freq[kj] +=1
    elif kj not in freq:
        freq[kj] =1

print(freq)

fre =freq.values()
max=float('-inf')
smax=float('inf')
for kk in fre:
    if kk >max:
        max =kk
for kk in fre:
    if kk < smax:
        smax=kk
print(max)
print(smax)

#duplicates
#numbers
dup=[2,3,4,5,6,6]
for exce in range(len(dup)):
    for dd in range (exce +1, len(dup)):
        if dup[dd]==dup[exce]:
            print(dup[exce])


#sort
gh =[1,3,6,8,9]

jk=sorted(gh,reverse=True)
print(jk)
#annagram

str1 = "listen"
str2 ="silent"

if sorted(str1)==sorted(str2):
    print("mk")
else:
    print("nk")



        

        
# non-reapet/uniq
app ="saikumar"

for jj in app:
    if app.count(jj)==1:
        print(jj)
        break


# remove the duplicates
app =[2,3,4,5,6,7,7,7]

ff =[]

for df in app:
    if df not in ff:
        ff.append(df)

print(ff)
# find the missing num

hj =[1,2,3,5]

for jk in range(1,6):
    hj.append(jk)

print(jk)

# owels, even and odd, count digits

alpha="saikumar_1122"

vowels =""

for hh in alpha:
    if hh not in "aeiou" and hh.isalpha():
        vowels +=hh
print(vowels)

# even and odd

kl =[2,3,4,5]
even=[]
odd=[]
for uk in kl:
    if uk % 2==0:
        even.append(uk)
    elif uk% 2==1:
        odd.append(uk)

print(even)
print(odd)

#count prime 

prime =7
count=0
for pre in range(1, 8):
    if prime % pre ==0:
        count +=1

if count ==2:
    print("prime")
else:
    print("not")


#digits
gh = 12344
total=0
for hk in str(gh):
    total +=int(hk)
print(total)    


# sorting

sort =[8,9,7,6,4,3]

for s1 in range(len(sort)):
    for s2 in range(len(sort)-1):
        if sort[s2] > sort[s2 + 1]:
            temp=sort[s2]
            sort[s2]=sort[s2+1]
            sort[s2+1]=temp

print(sort)


# sorting 
sort =[1,3,4,5,6,0]

