# try except assignment
# Task 1
try:
    num = 5/0
    print(num)
except ZeroDivisionError:
    print('division by zero is not possible!!')

# task 2
subjects = ["Americans ", "Indians "]
verbs = ["play ", "watch "]
objects = ["Baseball ", "Cricket "]

for a in subjects:
    for b in verbs:
        for c in objects:
            sent = str(a+b+c)
            print(sent)