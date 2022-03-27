list = ["Q1_22", "Q2_22", "Q3_22", "Q4_22", "Q1_23"]

list2 = [i.replace("_", "'") for i in list[0:4]]

print(list, list2)