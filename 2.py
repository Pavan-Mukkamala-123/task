str1 = input()
str2 = input()
last = str2[-1]
count = 0
for i in str1:
  if i == last:
    count += 1
print(count)    
