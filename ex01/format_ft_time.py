import time
from datetime import datetime


def format_ft_time():
    date = datetime.now()
    now = time.time()

    print(f"Second since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")
    print(date.strftime("%b %d %Y"))

if __name__ == "__main__":
    format_ft_time()