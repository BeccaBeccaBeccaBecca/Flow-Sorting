overallCategory = "x"
txt = "welcome [to the jungle]"


def main():
	f = open("flowCategories.txt", "r")
	global writeFile
	writeFile = open("separatedByCategories.txt", "w")
	for x in f:
  		parseCategory(x)

def parseCategory(txt):
	x = txt.split('[')
	phrase = x[0]
	category = x[1].split(']')[0]
	global overallCategory
	global writeFile
	if(overallCategory != category):
		overallCategory = category
		writeFile.write("\n\n[" + category + "]\n\n")
	writeFile.write(phrase + "\n")

main()