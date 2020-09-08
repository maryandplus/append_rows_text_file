#count lines of text file
num_lines = sum(1 for line in open(r"xxxx.txt"))
print(num_lines)


import os

#read all text files in a folder and append them to a list
folder = r'xxxXXXxxx'
asc_file=[]
for i in os.listdir(folder):
    if '.txt' in i:
        print(i)
        f = open(os.path.join(folder,i), "r")
        asc_file.append(f.readlines())
        f.close()
        
#append to a new file by row        
for counter in range(1,num_lines):
    for files in range(len(asc_file)):
        with open('output2.txt', 'a') as f1:
         
            f1.write(asc_file[files][counter].split(',')[2].replace('\n','') + ' ')

    with open('output2.txt', 'a') as f1:
        f1.write('\n')        
        f1.close()
