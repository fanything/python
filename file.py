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
<<<<<<< 0b14fd2ff4f76729fb80c51a64c5ead3fb653c0f
print("1")
print("2")
print("3")
=======
print("3")
print("4")
>>>>>>> 44
