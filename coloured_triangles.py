#row = 'RRGBG'

def triangle(row):
    if len(row) == 1:
        return row
    if len(row) > 1:
        new = []
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                new.append(row[i])
            if row[i] == 'R' and row[i+1] == 'G':
                new.append('B')
            if row[i] == 'R' and row[i+1] == 'B':
                new.append('G')
            if row[i] == 'G' and row[i+1] == 'B':
                new.append('R')
            if row[i] == 'G' and row[i+1] == 'R':
                new.append('B')
            if row[i] == 'B' and row[i+1] == 'G':
                new.append('R')
            if row[i] == 'B' and row[i+1] == 'R':
                new.append('G')
        
            if len(new) == 1:
                return new[0]  
            else:
                triangle(new)
    
        
print(triangle('RRRR'))