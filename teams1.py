#open new txt file to write 'w'
file = open("teams.txt",'w')

#add 5 sports teams
file.write("""Arsenal
Dortmound 
Liverpool
Real Madrid 
Manchester City
""")

#open file to read 
file = open("teams.txt", "r")

#read and display 1st line
print(file.readline())
file.readline()
file.readline()
#read and display 4th line
print(file.readline())

file.close()
