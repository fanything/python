import os

os.chdir('D:/python/chapter3')
print(os.path.exists('tt.txt'))
data = open('D:/python/chapter3/tt.txt')
for item in data:
        if not item.find(':') == -1:
                (name,work) = item.split(':',1)
                print(name,end='')
                print(' said: ',end='')
                print(work,end='')
data.close()
print('master')

print("1")
print("2")
print("3")
print("3")
print("4")
print("6")
print("5")
print("7")
