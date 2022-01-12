# Write a Python script to check whether a given key already exists in a dictionary.
# 20CE007 Jatan Bhimani

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present')
  else:
      print('Key is not present')
is_key_present(5)
is_key_present(9)