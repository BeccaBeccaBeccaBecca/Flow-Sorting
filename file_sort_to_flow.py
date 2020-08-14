import sys

overallCategory = "x"
txt = "welcome [to the jungle]"

def main():
	f = open("separatedByCategories.txt", "r")
	global writeFile
	writeFile = open("flowCategories.txt", "w")
	for x in f:
		if x != "\n":
  			parseCategory(x)

def parseCategory(txt):
	x = txt.split('[')
	global overallCategory
	global writeFile
	if len(x) > 1:
		overallCategory = x[1]
	else:
		phrase = x[0].split("\n")[0]
		writeFile.write(phrase + "[" + overallCategory)

main()