''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n=int(input())
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
main()

