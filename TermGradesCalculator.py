
prelim = float(input("Prelim grade: "))
midterm = float(input("Midterm grade: "))
finals = float(input("Final grade: "))

average = (prelim + midterm + finals) / 3
s = float("{:.2f}".format(average)) + 10.0

print("Final grade: ", s)