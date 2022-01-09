if __name__ == '__main__':
    n = int(input())
    i = n
    numlist = []
    resultlist = []
    while (i > 0):
      i = i - 1
      r = i * i
      numlist.append(i)
      resultlist.append(r)
    if (i == 0):
      numlist.sort()
      resultlist.sort()
      for a in resultlist:
        print (a)