s1 = 'abarrabcakkcadkcdabbaarra'
s2 = 'barrackadabadckdbaabararaa'

def editDistance(s1, s2):
    s1 = ' ' + s1 #first raw enpty in matrix
    s2 = ' ' + s2 #first column in matrix empty
    matrix = {} 
    s1_len = len(s1)
    s2_len = len(s2)
    for i in range(s1_len):
        matrix[i, 0] = i
    for j in range (s2_len):
        matrix[0, j] = j
    for j in range(1, s2_len):
        for i in range(1, s1_len):
            if s1[i] == s2[j]:
                matrix[i, j] = matrix[i - 1, j - 1]
            else:
                matrix[i, j] = min(matrix[i - 1, j] + 1, matrix[i, j - 1] + 1, matrix[i - 1, j -1] + 1)
    return matrix[s1_len - 1, s2_len - 1]

print editDistance(s1, s2)