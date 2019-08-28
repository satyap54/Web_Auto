import os,shutil

f=os.listdir('/home/satyabrat/P')
if("DotJavaFiles" in f):
	os.rmdir("/home/satyabrat/P/DotJavaFiles")

for foldername,subfolder,filename in os.walk('/home/satyabrat/P/CBlocks/'):
	#print(f'Folder:{foldername}')
	split_name=foldername.split('/')
	folder_name=split_name[-1]

	print(f"Folder created:{folder_name}")

	folder_create=os.path.join('../DotJavaFiles',folder_name)
	os.mkdir(folder_create)

	for file in filename:
		if(file.endswith('.java')):
			print(file+" ")
			shutil.copy(os.path.join(foldername,file),folder_create+"/")

	print("\n")