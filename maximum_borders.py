trials=int(input("Enter number of trials: "))
for trial in range(trials):
    randc=(list(map(int,(input(f"Enter row then space and column for trial {trial}: ").split(' ')))))
    rows,cols=randc[0],randc[1]
    table=[[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        input_row=list(input(f"Enter the elements of row {i}: "))
        for j in range(cols):
            table[i][j]=input_row[j]
    row_hashes={}          
    col_hashes={}              
    for k in range(rows):
        for m in range(cols):
            if table[k][m] == "#":
                if k not in row_hashes:
                    row_hashes[k]=[]
                row_hashes[k].append(m)
    
    for l in range(cols):
        for n in range(rows):
            if table[n][l] == "#":
                if l not in col_hashes:
                    col_hashes[l]=[]
                col_hashes[l].append(n)
    # print(row_hashes)
    # print(col_hashes)
    count=1
    num_counts=[]    
    for num in row_hashes:
        for cons in row_hashes[num]:
            # print(f"The list is {len(row_hashes[num])} items long")
            # print(f"The current value index is {cons}")
            # print(f"the list is {row_hashes[num]}")
            # print(f"the last value is {row_hashes[num][-1]}")

# check if cons is not greaterthan or equal to
            if cons < row_hashes[num][-1]:
                # print(f"incrementin by one is {cons+1}")
                indexof=row_hashes[num].index(cons)
                # print(f"The index of is {indexof}")
                # print(f"The value to be compared with is {row_hashes[num][indexof+1]}")
                if (cons+1) == (row_hashes[num][indexof+1]):
                    count+=1 
                elif count > 1:
                    num_counts.append(count)
                    count=1

        # print(count)                
        if count > 1:
            num_counts.append(count)
        else:
            num_counts.append(1)     
        count=1    
    # print(num_counts)

    counter=1
    # print("........................................................................................")
    for num in col_hashes:
        for cons in col_hashes[num]:
            # print(f"The list is {len(col_hashes[num])} items long")
            # print(f"The current value index is {cons}")
            # print(f"the list is {col_hashes[num]}")
            # print(f"the last value is {col_hashes[num][-1]}")
# check if cons is not greaterthan or equal to
            if cons < (col_hashes[num][-1]):
                # print(f"incrementin by one is {cons+1}")
                indexof=col_hashes[num].index(cons)
                # print(f"The value to be compared with is {col_hashes[num][indexof+1]}")
                if (cons+1) == (col_hashes[num][indexof+1]):
                    counter+=1
                elif counter > 1:
                    num_counts.append(counter)
                    counter=1    

        # print(counter)                
        if counter > 1:
            num_counts.append(counter)
        else:
            num_counts.append(1)    
        counter=1    
    # print(num_counts)
    print(max(num_counts))