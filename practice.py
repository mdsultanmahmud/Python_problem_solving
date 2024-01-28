'''
problem --- 19
q: Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.


code: 
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def getColor(l_1, l_2):
    print(f"Differenc between set one and set two is :\n {l_1.difference(l_2)}")
    print(f"Differenc between set two and set one is :\n {l_2.difference(l_1)}")

getColor(color_list_1, color_list_2)
''' 
