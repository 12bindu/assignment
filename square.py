def main():
    n = read('enter the value of the n:')
    display(area(n),perimeter(n))

def read(msg):
    return int(input(msg))

def area(n):
    return n**2

def perimeter(n):
    return 4*n
def display(area,perimeter):
    print(f'the area and the perimeter of the square is{area},{perimeter}')
main()