def solution(survey, choices):
    answer = ''
    dic = { 'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0 }
    for i,j in zip(survey, choices):
        if j < 4 :
            dic[i[0]] +=  4 - (j%4)
        elif j > 4 :
            dic[i[1]] += j - 4    

    RCJA = ['R','C','J','A']
    TFMN = ['T','F','M','N']

    for x,y in zip(RCJA, TFMN):
        if dic[x] < dic[y] :
            answer += y 
        else:
            answer += x 
          
    return answer
