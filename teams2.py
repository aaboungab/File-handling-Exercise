#Open read only 
file = open("teams.txt",'r')

line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
line4 = file.readline()
line5 = file.readline()

#group all the variable that are not going to be changed
lines = line2, line3, line4, line5

#Open as write 
file = open("teams.txt",'w')
#overwrite line1 with new string
line1 = "This is a new line\n" 
file.write(line1)
#add previous lines
file.writelines(lines)
file.close

print(line1)
print(lines)

