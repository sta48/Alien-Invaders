def new():
    column = []
    l = ['a', 'a', 'b', 'b', 'c', 'c']
    # y = [alien1,alien2,alien3]
    r = 0
    for n in range(5):
        row= []
        c = 0
        for b in range(12):
            row.append(l[r])
            l.append(l[r])
            # print ('l is' + str(l))
            # print ('r is' + str(r))
        column.append(row)
        # print('column is' + str(column))
        c = c + 1
        # print('c = '+str(c))
        r = r + 1
        # print('r = '+str(r))
    return column

    [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
     ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
     ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
     ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
     ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']]
