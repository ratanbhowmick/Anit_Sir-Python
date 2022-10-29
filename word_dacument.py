file_name = input("Enter file name:")

file1 = open(file_name, "r")

d = dict() 
  
print("\n File Contents are:\n")

for line in file1:
    print(line, end='')
    line = line.strip() 
  
    line = line.lower() 
    words = line.split(" ") 
  
    for word in words: 
        if word in d: 
            d[word] = d[word] + 1
        else: 
            d[word] = 1

print("\n\nNumber of occurrences of each word in given text file is:")  
print("\n ===============\n")  

for key in list(d.keys()): 
    print(key, ":", d[key]) 

file1.close()