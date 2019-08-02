f = open("charge.txt","r",encoding="utf-8")
f2 = open("charge2.txt","w",encoding="utf-8")
for line in f.readlines():
	line = line.replace("	",".")
	line = line.replace("..",".").replace("\n","")
	f2.writelines(line)
	f2.write("\n")