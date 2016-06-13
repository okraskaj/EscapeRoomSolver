def main():
    print("wpisz baze")
    base= int(input())
    matrix = [[0 for x in range(base)]for y in range(base)]
    col_sum = [0 for x in range(base)];
    row_sum =[0 for x in range(base)];


    print("Wpisz góre")
    for i in range(base):
        col_sum[i] = int(input())

    print("Wpisz lewą")
    for i in range(base):
        row_sum[i] = int(input())

    print("Wpisz dane")
    for i in range(base):
        for j in range(base):
            print("(" + str(i) + "," + str(j) + ")")
            matrix[i][j] = int(input())

    for i in range(base):
        for j in range(base):
            print(str(matrix[i][j])+" ", end="")
        print()

    base2 = pow(base, 2)
    base4 = pow(base, 4)
    format_mod = '#0' + str(2 + base2) + 'b'
    my_range = pow(2, base4)
    for a in range(my_range):
        print("postep :"+str((a*100)/my_range)+"%")
        curr_col_sum = [ 0 for x in range(base)]
        curr_row_sum = [ 0 for x in range(base)]
        for i in range(base):
            for j in range(base):
                if(int(format(a,format_mod)[i*base+j+2])):
                    curr_row_sum[i]+= matrix[i][j]
                    curr_col_sum[j]+= matrix[i][j]
        ok = 1
        for i in range(base):
            if (curr_col_sum[i] != col_sum[i]) or (curr_row_sum[i] != row_sum[i]):
                ok = 0
        if ok:
            print("zwyciestwo")
            for i in range(base):
                for j in range(base):
                    if int(format(a,format_mod)[i*base+j+2]):
                        print(str(matrix[i][j])+" ",end="")
                    else:
                        print("  ", end="")
                print()
            break

if __name__ == "__main__":   main()
