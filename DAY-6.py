''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n=int(input())
    c=0
    while(n>0):
        n=n//10
        c=c+1
    print(c)

main()

