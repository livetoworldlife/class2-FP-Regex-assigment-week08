import re

# read txt file
with open("regex_sum_42.txt",encoding="utf-8") as file:
    oku = file.read()
    


list_for_sum = list()
# get the numbers srt
match = re.findall(r'[0-9]+', oku)
for i in match:
    list_for_sum.append(int(i))
    
# convert str to int
sum_of_txt = sum(list_for_sum)

print("Total of numbers in txt :",sum_of_txt)
print("Number of matches :", len(match))