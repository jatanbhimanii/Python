# Write a Python script to concatenate following dictionaries to create a new one.

# Sample Dictionary :

# dic1={1:10, 2:20}

# dic2={3:30, 4:40}

# dic3={5:50,6:60}

# 20CE007 Jatan Bhimani

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d1 = {7:70, 8:80, 9:90, 10:100}
d2 = {11:110, 12:120}

d1.update(d2)
d.update(d1)
print(d)