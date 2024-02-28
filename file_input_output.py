############################### File I/O in python ####################

'''file = open('demo.txt','r')
data = file.read()
print(data)
file.close()'''

'''file = open('demo.txt','r')
data = file.read(5)
print(data)
file.close()'''

'''file = open('demo.txt','r')

line1 = file.readline()

print(line1)
    
line2 = file.readline()

print(line2)'''

'''f = open('nasim.txt','a')

f.write('Nasim Uddin')

f.close()'''


'''f = open('demo.txt','w')

f.write('Nasim Uddin')

f.close()'''

'''f = open('demo.txt','a')

f.write('\n is a data scientiest ')
f.close()'''

'''f = open('demo.txt','r+')
f.write('hi')
print(f.read())
f.close()'''

'''f = open('demo.txt','w+')
f.write('hi')
#print(f.read())
f.close()'''

'''f = open('demo.txt','a+')
f.write('nasim')
print(f.read())
f.close()'''

'''with open('demo.txt','r') as f:
    data = f.read()
    print(data)'''

'''with open('demo.txt','w') as f:
    data = f.write('new values')'''

'''import os

os.remove('demo.txt')'''

########################## pactices question ####################

'''with open('demo.txt','w') as f:
    f.write("hi every one \n I am learning file I/O \n")
    f.write("using Java \n I like programing Java")'''

'''with open('demo.txt','r') as f:
    data = f.read()

new_data = data.replace('Java','python')
print(new_data)

with open('demo.txt','w') as f:
    data = f.write(new_data)'''

'''word = 'learning'

with open('demo.txt','r') as f:
    data = f.read()
    if (data.find(word)!= -1 ):
        print('found')
    else:
        print('not found')'''

'''def chack_for_word():
    word = 'learning'
    with open('demo.txt','r') as f:
        data = f.read()
        if (data.find(word) != -1):
            print('found')
        else:
            print('not found')
   
chack_for_word()'''

'''def chack_for_word():
    word = 'learning'
    with open('demo.txt','r') as f:
        data = f.read()
        if (word in data):
            print('found')
        else:
            print('not found')
            
chack_for_word()

def chack_word():
    word = 'programing'
    data = True
    line_no = 1
    
    with open('demo.txt','r') as f:

        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            
            line_no += 1

    return -1

x = chack_word()
print(x)'''

'''with open('number.txt','r') as f:
    data = f.read()
    print(data)

    num = ""

    for i in range(len(data)):
        if (data[i] == ','):
            print(int(num))
            num = ""
        else:
            num += data[i]'''


count = 0

with open('number.txt','r') as f:
    data = f.read()

    nums = data.split(',')

    for val in nums:
        if (int(val) % 2 == 0):
            count += 1

        
print(count)            
        
        
            














