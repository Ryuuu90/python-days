import sys


def whatis():
    if len(sys.argv) == 1: 
        return
    assert len(sys.argv) == 2 , "more than one argument is provided"
    number = sys.argv[1]
    assert number.lstrip('-+').isdigit() ,"argument is not an integer"
    if int(number) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
if __name__ == "__main__":
    try:
        whatis()
    except AssertionError as error:
        print(f"AssertionError: {error}")
        
    

