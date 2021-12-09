def clean(floor):
    m=len(floor)
    n=len(floor[0])
    for i in range(m):
        if i%2==0:
            for j in range(n):
                print("Enter the status of the location "+sample_floor[i][j])
                floor[i][j]=int(input())
                if(floor[i][j]==1):
                    print("the vaccum cleaner is at location "+sample_floor[i][j])
                    print("STATUS:DIRTY")
                    floor[i][j]=0
                    print_floor(floor,i,j,1)
                else:
                    print("the vaccum cleaner is at location "+sample_floor[i][j])
                    print("STATUS:CLEAN")
                    print_floor(floor,i,j,0)

        else:
            for j in range(n-1,-1,-1):
                print("Enter the status of the location "+sample_floor[i][j])
                floor[i][j]=int(input())
                if(floor[i][j]==1):
                    print("the vaccum cleaner is at location "+sample_floor[i][j])
                    print("STATUS:DIRTY")
                    floor[i][j]=0
                    print_floor(floor,i,j,1)
                else:
                    print("the vaccum cleaner is at location "+sample_floor[i][j])
                    print("STATUS:CLEAN")
                    print_floor(floor,i,j,0)
    print("STATUS: ALL STATES CLEANED")
    print_floor(floor,i,j,2)
    return
def print_floor(floor, row, col,m): # row, col represent the current vacuum cleaner position
    if m==0:
        print(sample_floor[row][col]+ " is clean vaccume cleaner move to the next location")
        print(f"""
        {floor[0]}
        {floor[1]}
        """)
        print("-----------------")
    elif m==1:
        print(sample_floor[row][col]+ " was dirty vaccume cleaner cleaned and moving to the next location")
        print(f"""
        {floor[0]}
        {floor[1]}
        """)
        print("-----------------")
    else:
        print(f"""
        {floor[0]}
        {floor[1]}
        """)
# Test 1
floor = [[0,0],
         [0,0]]
sample_floor=[["A","B"],
              ["C","D"]]
print("The sample floor is :")
print(f"""
      {sample_floor[0]}
      {sample_floor[1]}
      """
      )

clean(floor)
