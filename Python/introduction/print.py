if __name__ == '__main__':
    n = int(input('num:?'))
    listn = []
    listns = ""
    listn.append(n)
    while (n > 1):
      n = n - 1
      listn.append(n)
    if (n == 1):
      listn.sort()
      for a in listn:
        listns += str(a)
      print(listns)