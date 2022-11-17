#!/usr/bin/python3
def pascal_triangle(n):

    if n <= 0:
        return([])
    
    else:
        my_list = []
        
        for i in range(n):
            temp_list = []
            
            for j in range(i+1):
                
                if j == 0 or j == i:
                    temp_list.append(1)
                else:
                    temp_list.append(my_list[i-1][j-1]  +  my_list[i-1][j])
            my_list.append(temp_list)  
        return(my_list)
