import os
checker = input("Enter the name of the binary: ")
print('Checking file /usr/bin/'+checker)

if not os.path.exists("/home/sahil/checker_string"):
	os.system("mkdir /home/sahil/checker_string")

os.system(f'strings /usr/bin/{checker} > /home/sahil/checker_string/{checker}.txt')	
os.system("gedit /home/sahil/checker_string/"+checker+".txt")
