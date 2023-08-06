import random

result=''
file = open('Hello World.txt','w')
target = 'Hello World.py'

charList = [chr(i) for i in range (32,127)]

while result !=target:
    char = random.choice(charList)
   
    l = len(result)
    
    if(char==target[l]):
        result+=char
        file.write(result+'<----------------------\n')
        continue
    else:
        file.write(result+char+'\n')

file.close()
    
    
        
