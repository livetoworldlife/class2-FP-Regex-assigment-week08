# Create a file “numbers.txt” and write the numbers 1 to 10 into the file.. 

with open("numbers.txt","w+") as f:
    for i in range(10):
        f.write("Number: %d\r\n" % (i+1))
