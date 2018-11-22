def print_line(char,times):

    print(char * times)

def print_lines(char,times):
    """打印多行分割线"""
    row = 0

    while row < 6:

        print_line(char,times)

        row += 1

name = "ph"