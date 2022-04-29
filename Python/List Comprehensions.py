if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    l2 = []
    
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                l1 = [i, j, k]
                if sum(l1) != n:
                    l2.append(l1) 
            
    print(l2)
    #if it works append 