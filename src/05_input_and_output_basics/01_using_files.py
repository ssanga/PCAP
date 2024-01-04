with open('xmen.txt','w+') as my_file:
    my_file.write('Beast\n')
    my_file.write('Phoenix\n')
    my_file.writelines(['Cyclops\n',
                'Bishop\n',
                'Nightcrawler\n'])

    my_file.seek(0)
    for line in my_file.readlines():
        print(line)

with open('xmen.txt','r') as my_file:
    print(my_file.read())

# bytes
with open('xmen.txt','rb') as f:
    print(f.read())
    print(f.readlines())

with open('xmen.txt','rb') as f:
    b_array = bytearray(10)
    f.readinto(b_array)
    print(b_array)

# sys
import sys
print(sys.stdout.write("Testing\n"))
print(sys.stderr.write("ERROR\n"))