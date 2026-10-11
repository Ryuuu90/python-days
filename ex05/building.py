import sys


def count_and_check(text: str) -> None:
    uppers = 0
    lowers = 0
    spaces = 0
    digits = 0
    p_marks = 0
    for char in text : 
        if char.isupper():
            uppers += 1
        elif char.islower():
            lowers += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1
        else:
            p_marks += 1
    print(f'The text contains {len(text)} characters:')
    print(f'{uppers} upper letters')
    print(f'{lowers} lower letters')
    print(f'{p_marks} punctuation marks')
    print(f'{spaces} spaces')
    print(f'{digits} digits')
        


def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"

        if len(sys.argv) == 2 and sys.argv[1]:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = sys.stdin.readline()

        count_and_check(text)

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except (EOFError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    main()
            
        