

with open('input.txt') as f:
    stringlines = f.readlines()

directions = []
for line in stringlines:
    direction = line.split()
    directionParsed = [direction[0], int(direction[1])]
    directions.append(directionParsed)

positionDepth = 0
positionHorizontal = 0
aim = 0

for direction in directions:
    if direction[0] == "forward":
                positionHorizontal += direction[1]
                positionDepth += direction[1] * aim
    if direction[0] == "up":
                aim -= direction[1]
    if direction[0] == "down":
                aim += direction[1]


print("positionDepth: " + str(positionDepth))
print("positionHorizontal: " + str(positionHorizontal))
print("multiplied: " + str(positionHorizontal * positionDepth))
