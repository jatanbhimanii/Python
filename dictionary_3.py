# Write a Python program to sum all the items in a dictionary.
# 20CE007 Jatan Bhimani

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# d1 = {7:70, 8:80, 9:90, 10:100}

values = d.values()
total = sum(values)
print(total)