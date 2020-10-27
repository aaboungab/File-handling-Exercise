file = open("teams.txt",'r')
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
line4 = file.readline()
line5 = file.readline()
lines = line2, line3, line4, line5

file = open("teams.txt",'w')
line1 = "This is a new line\n" 
file.write(line1)
file.writelines(lines)
file.close
print(line1)
print(lines)

