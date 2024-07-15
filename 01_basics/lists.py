football_positions = ["striker","winger","centre back","defensive midfielder"]
print(football_positions)

print(football_positions[1])  # winger

# slicing and dicing

print(football_positions[-1]) # defensive midfielder
print(football_positions[1:3]) # ['winger','centre back']
print(football_positions[:2])  # ['striker','winger']
print(football_positions[2:])  # ["centre back","defensive midfielder"]

# changing content

football_positions[2] = "full back"
print(football_positions) #['striker', 'winger', 'full back', 'defensive midfielder']

# This will not work as expected

football_positions[2:3]="right back"
print(football_positions) #['striker', 'winger', 'r', 'i', 'g', 'h', 't', ' ', 'b', 'a', 'c', 'k', 'defensive midfielder']

# Let's reset the list
football_positions = ["striker","winger","centre back","defensive midfielder"]

# This will work as expected
football_positions[2:3]=["right back"]
print(football_positions) # ['striker', 'winger', 'right back', 'defensive midfielder']