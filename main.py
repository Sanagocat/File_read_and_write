#read data.txt
f = open("data.txt","r") #file read mode "r"

count=0
for line in f:
  count=count+1
  new_line = line.rstrip()
  print(new_line)
  if(new_line=="bravo"):
    print(">>> GOT IT! ")

f.close()
    
#HOW MANY 0K0K IN problem.txt
e = open("problem.txt","r") #file read mode "r"

count=0
for line in e:
  new_line_2 = line.rstrip()
  if new_line_2 == "0K0K":
    count=count+1

print("problem 1 : "+ str(count))
e.close()

ff = open("result.txt","w") #file write mode "w" - Erase all contents
ff.write("Prob 1 - the amount of 0K0K is " + str(count) +"\n") #\n = nextline
ff.close()


#HOW MANY 0K0K IN problem.txt
e = open("problem2.txt","r") #file read mode "r"

count2=0
for line in e:
  new_line_2 = line.rstrip()
  if new_line_2 == "0K0K":
    count2=count2+1

print("problem 2 : "+ str(count2))
e.close()


ff = open("result.txt","a") #append mode - append write
ff.write("Prob 2 - the amount of 0K0K is " + str(count2) + "\n")
ff.close()



ff = open("result.txt","a")
ff.write("HAHAHAHAHAHA")
ff.close()





#1. Read Data Base and show it as a line format (JBSONG, Math:90, ENG:60, ART:30)
#2. Write Line Format to result.txt
#3. Calculate Average of each Student and Show it (JBSong : 60)
#4. Write Average to Average.txt
