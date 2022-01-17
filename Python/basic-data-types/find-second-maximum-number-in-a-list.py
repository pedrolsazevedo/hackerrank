if __name__ == '__main__':

  n = int(input("Total: "))
  arr = list(map(int,input("Notes: ").strip().split()))[:n]

  n = 10
  arr = [6, 6, 6, 6, 6, 6, 6, 6, 6, 5]
  m = max(arr)
  x = len(arr)

  arr.sort(reverse=True)
  while max(arr) == m:
    arr.remove(max(arr))

print (max(arr))
#  while max(arr) < m :
#      if g == m:
#    arr.remove(max(arr))
#    print("Removed: ", max(arr))
#    print("Remain:",arr)
#  print(arr, "max: ", max(arr))



#Total: 10
#Notes: 6 6 6 6 6 6 6 6 6 5