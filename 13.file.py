f = open ("demo.txt","a")
data = f.write("\nI am appending the data right now.")
print (data)

f.close()

#File creation 
creation = open ("newfile.txt","w")
line = f.write ("I am making the new file right now.")
