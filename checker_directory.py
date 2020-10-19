import os
print('Converting each binary to text file')
if not os.path.exists(os.getcwd()+"/text"):
		os.system("mkdir {os.getcwd()}/text")
for file in os.listdir():
	print('Checking file {file}')
	os.system(f"strings {file} > /home/sahil/text/{file}.txt")	

