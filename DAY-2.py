''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    var = input()
    try:
        val = int(var)
        print("This input is of type Integer.", end="")
    except ValueError:
        try:
            val = float(var)
            print("This input is of type Float.", end = "")
        except ValueError:
            try:
                val = str(var)
                print("This input is of type string.", end = "")
            except ValueError:
                print("This is something else.", end="")

main()

