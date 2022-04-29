if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    arr.sort(reverse=True)
    s = []
    for i in arr:
       if i not in s:
          s.append(i)
          
    print(s[1])
