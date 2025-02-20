def main():
    letterdict = {}
    with open("books/frankenstein.txt") as f:
        text = f.read()
        for i in text:
            if i.lower() not in letterdict:
                letterdict[i.lower()] = 1
            else:
                letterdict[i.lower()] += 1
    for j in letterdict:
        if j.isalpha():
            print(f"The '{j}' character was found {letterdict[j]} times")

if __name__ == "__main__":
    main()