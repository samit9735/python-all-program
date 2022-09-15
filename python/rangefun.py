import random 
random_list=list(range(0,25))
random.shuffle(random_list)
print(f"Random list=\n{random_list}",end=" ")
def sort_print_highlight(data,copy_data):
    for i_2 in range(0,len(data)):
        if copy_data[i_2] != data[i_2]:
            print(f"\033[1;33m{data[i_2]}",end='')
        else:
            print(f"\033[1;36m{data[i_2]}",end='')
def bubblesort(data):
    is_sorted=False
    while not is_sorted:
        is_sorted=True
        for i in range(0,len(data) - 1):
            if data [i]> data[i+1]:
                is_sorted=False
                copy_data=data.copy()
                data[i],data[i+1]=data[i+1],data[i]
                print("\n")
                sort_print_highlight(data,copy_data)
                
                
    return data
print(f"\n\n\033[1;37mSorted list = \n{bubblesort(random_list)}")