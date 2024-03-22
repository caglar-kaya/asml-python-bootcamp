motherHeight = 1.50
fatherHeight = 1.75
brotherHeight = 1.65
sisterHeight = 1.80

family_heights = [motherHeight, fatherHeight, brotherHeight, sisterHeight]

print("Total family members : ", len(family_heights))
print("List of Family Heights : ", family_heights)

average_height = sum(family_heights) / len(family_heights)

print("Average Height of the family", round(average_height, 2), "meters")

tallest_height = max(family_heights)
shortest_height = min(family_heights)

print("Tallest family member has a height of", tallest_height, "meters")
print("Shortest family member has a height of", shortest_height, "meters")

x = ["a", "b", "c", "d"]

print(x[1:3])
