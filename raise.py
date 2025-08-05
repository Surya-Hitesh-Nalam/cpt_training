try:
    num=11
    print(num)
    raise ValueError
except:
    print("An Exception Occured")
    raise ValueError
finally:
    print("This is finally block")
    print("Bye")