new_list = [1, 2, 3]
result = new_list[0]

if 1 in new_list:
  print(True)

for  n in new_list:
  if n == 1:
    print(True)

    break  
  
# adding the list
new_list.append(4)
new_list.append(5)
new_list.append(6)
print(new_list)

#extend the list
new_list.extend([7, 8, 9])
print(new_list)
