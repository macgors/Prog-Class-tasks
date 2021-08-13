try:
    a = int(input('Enter number:'))
    print(f"Value is {'even' if a % 2 == 0 else 'odd'}")
except ValueError:
    print('Not an integer')