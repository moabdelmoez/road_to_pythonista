def doubleStuff(alist):
    """Overwrite each element in aList with double its value."""

    for position in range(len(alist)):
        alist[position] = alist[position] * 2

def main():
    things = [2, 5, 9]
    print(things)

    doubleStuff(things)
    print(things)

if __name__ == "__main__":
    main()
