xCounts = [5, 2, 5, 2, 2]

# for lineXCount in xCounts:
#     xCount = 0
#     lineStr = ''
#     while xCount < lineXCount:
#         lineStr += 'x'
#         xCount += 1
#     print(lineStr)

for lineXCount in xCounts:    
    lineStr = ''
    for x in range(0, lineXCount):
        lineStr += 'x'
    print(lineStr)