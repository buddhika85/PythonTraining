# L shape

x_counts = [1, 1, 1, 1, 5]

for line_x_count in x_counts:    
    line_str = ''
    for x in range(line_x_count):
        line_str += 'x '
    print(line_str)