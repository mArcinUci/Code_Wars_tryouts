def triangle(row):
    new_row = []
    if len(row) > 1:
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                new_row.append(row[i])
            if row[i]=='B' and row[i+1]=='G':
                new_row.append('R')
            if row[i]=='B' and row[i+1]=='R':
                new_row.append('G')
            if row[i]=='G' and row[i+1]=='R':
                new_row.append('B')
            if row[i]=='G' and row[i+1]=='B':
                new_row.append('R')
            if row[i]=='R' and row[i+1]=='G':
                new_row.append('B')
            if row[i]=='R' and row[i+1]=='B':
                new_row.append('G')
        return triangle(new_row)
    else:
         return row[0]
    
print(triangle('BBR'))