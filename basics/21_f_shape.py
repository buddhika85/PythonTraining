x_counts = [5, 2, 5, 2, 2]

# for line_x_count in x_counts:
#     x_count = 0
#     line_str = ''
#     while xCount < line_x_count:
#         line_str += 'x'
#         x_count += 1
#     print(line_str)

for line_x_count in x_counts:    
    line_str = ''
    for x in range(0, line_x_count):
        line_str += 'x'
    print(line_str)