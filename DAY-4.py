''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n=int(input())
    if(n<10):
        print('I am happy as having no responsibilities.') 
    elif(n>=10 and n<18):
        print('I am still happy but starts feeling pressure of life.')
    else:
        print("I am very much happy as i handled the pressure very well.")
main()

