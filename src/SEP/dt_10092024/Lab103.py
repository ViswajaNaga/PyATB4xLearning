# with open("testdata.txt",'r') as file:
file=open("testdata.txt",'r')  # line 2 and line 1 represents same but in different ways 1-using with 2-without using with
lines=file.readlines()
for line in lines:
    print(line)
