#Write a function to compute 5/0 and use try/except to catch the exceptions.
def impossible_division():
    try:
        result = 5 / 0
        print("Result:", result)
    except ZeroDivisionError as e:
        print("Error:", e)

impossible_division()
