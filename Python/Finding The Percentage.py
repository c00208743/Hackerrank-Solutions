if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    avgDict = {}
    for k,v in student_marks.iteritems():
        # v is the list of grades for student k
        avgDict[k] = format(float(sum(v)/ int(len(v))), '.2f')
    
    print(avgDict[query_name])
