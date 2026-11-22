# # rev
# str = "sai kumar"

# dd =""

# for ng in str.split():
#     word=""

#     for ch in ng:
#         word = ch + word

#     dd = dd + word + " "

# print(dd.strip())

str = "sai kumar"

dd ="" 

for hj in str.split():
  wrd=""
  for gg in hj:
    wrd = gg + wrd
  dd += wrd +" "

print(dd)



# st = "dud djk"

# fg =""

# for kk in str.split():
#     fg = kk +" "+fg 
# print(fg)

rev = 1234

strp =0

# for res in reversed(str(rev)):
#     strp = int(res) + strp * 10
# if rev == strp:
#     print("pal")
# else:
#     print("not")

# greatest and less than

grt =[22,33,4,5,6,21,7,89]

gt =float("-inf")
sgt=float("-inf")
ssgt=float("-inf")
ls=float("inf")
sls=float("inf")

for hh in grt:
  if hh>gt:
    sgt=gt
    gt=hh
  elif hh> sgt and gt !=hh:
    ssgt=sgt
    sgt=hh
  elif hh>ssgt and gt !=hh and sgt !=hh:
    ssgt=hh
  elif hh<ls:
    sls=ls
    ls=hh
  elif hh<sls and ls !=hh:
    sls=hh

print(gt)
print(sgt)
print(ssgt)
print(ls)
print(sls)  

# count

cut ="saikumar"

ch = "a"

count =0

for vv in cut:
  if vv ==ch:
    count +=1

print(count)

# frequency
fr ="saikumar"
freq={}

for jj in fr:
  if jj in freq:
    freq[jj]+=1
  elif jj not in freq:
    freq[jj]=1
print(freq)

# max and min accrance
fre =freq.values()
maxs=float("-inf")

for nm in fre:
  if nm>maxs:
    maxs=nm

print("Maximum:", maxs)

# find and remove the duplicates

stg ="saikumar"
gg=""
for dd in stg:
  if dd not in gg:
    gg +=dd

print(gg)

# find the duplicates
stg ="saikumar"
dd=""

for gg in range(len(stg)):
  for gg1 in range(gg+1 ,len(stg)):
    if stg[gg]==stg[gg1]:
      print(stg[gg])
# sort
srt =[9,2,3,4,5,1]

for dd in range(len(srt)):
    for hk in range(len(srt)-1):
      if srt[hk]<srt[hk +1]:
        temp =srt[hk]
        srt[hk]=srt[hk+1]
        srt[hk+1]=temp

print(srt)


# range
rg =[1,2,3,4,6]

for rl in range(1,7):
  if rl not in rg:
    print(rl)
#owels
vv ="saikumar"
owels=""
cons=""

for vg in vv:
  if vg in "aeiou" and vg.isalpha():
    owels +=vg
  else:
    cons +=vg
  
print(owels)
print(cons)
#prime
prime=7
count=0

for p in range(1,8):
  if prime % p == 0:
    count +=1
print(count)


#even and odd
gh =[2,3,45,6]

even=[]
odd=[]

for g in gh:
  if g % 2==0:
    even.append(g)
  else:
    odd.append(g)  

print(even)
print(odd)

# sum the digit

su =1234
ff=0
for f in str(su):
    ff+=int(f)
print(ff)