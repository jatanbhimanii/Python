# Write a Python script to add a key to a dictionary.		Sample Dictionary : {0: 10, 1: 20}		Expected Result : {0: 10, 1: 20, 2: 30}
# 20CE007 Jatan Bhimani

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# d1 = {7:70, 8:80, 9:90, 10:100}

d.update({7:70, 8:80})
print(d)