def find(astring, achar):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    index = 0
    found = False
    while index < len(astring) and not found:
        if astring[index] == achar:
            found = True
        else:
            index = index + 1
    if found:
        return index
    else:
        return -1

print(find("mostafa", "t"))
