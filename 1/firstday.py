

with open('previousmeasurements.txt') as f:
    stringlines = f.readlines()

lines = []
for line in stringlines:
    lines.append(int(line))

previousMeasurement = 100000000
depthIncreased = 0
depthIncreasedRollingAvg = 0
for lineNum in range(len(lines)):
    if lines[lineNum] > previousMeasurement:
        depthIncreased += 1
    previousMeasurement = lines[lineNum]

    if lineNum > 2:
        previousThreeAvg = lines[lineNum -1] + lines[lineNum -2] + lines[lineNum -3]
        thisThreeAvg = lines[lineNum -0] + lines[lineNum -1] + lines[lineNum -2]
        if previousThreeAvg < thisThreeAvg:
            depthIncreasedRollingAvg += 1

print("Depth increases: " + str(depthIncreased))
print("Depth increases (rolling): " + str(depthIncreasedRollingAvg))
