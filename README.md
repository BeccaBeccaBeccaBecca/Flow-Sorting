# Flow Sorting
 sort categories into the necessary brackets

 FROM flowxo (Flowcategories.txt) TO groups (separatedbycategories.txt)

 python file_sorting.py

 FROM groups (separatedbycategories) TO flowxo (Flowcategories)

python file_sort_to_flow.py 

changes will be in the txt files, can then copy and past what is in flowcategories to the flowxo website
