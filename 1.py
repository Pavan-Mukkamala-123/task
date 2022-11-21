n = int(input())
if n == 0:
  print(0)
nums = []:
  n, r = divmod(n, 3)
  nums.append(str(r))
print(''.join(reversed(nums)))
