from ft_filter import ft_filter 
import sys

def main():
    """ Filter words longer than the given length."""
    try:
        assert len(sys.argv) == 3, "more than one argument is provided"
        text = sys.argv[1]
        assert text.isascii and all( char.isalpha() or char.isspace() for char in text), "the arguments are bad"
        assert sys.argv[2].lstrip("-").isdigit(), "the arguments are bad"
        length = int(sys.argv[2])
        words = text.split(" ")
        res = list(ft_filter(lambda word: len(word) > length, words))
        print(res)
    except (AssertionError, ValueError) :
        print("AssertionError : the arguments are bad")

if __name__ == "__main__":
    main()


    
