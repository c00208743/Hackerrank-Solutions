if __name__ == '__main__':
    
    l2 = []
    scores = []
    
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        l1 = []
        
        l1.append(name)
        l1.append(score)
        
        scores.append(score)
        
        l2.append(l1)
        
    
    l2 = sorted(sorted(l2, key = lambda x : x[0]), key = lambda x : x[1], reverse = False) 
    scores = list(dict.fromkeys(scores))
    scores.sort()
    
    i = int(0)
    while i != len(l2):
        if l2[i][1] == scores[1]:
            print(l2[i][0])
        i += 1
    
    
    
        
        
