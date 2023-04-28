def binary_search(a,x):
    first_pos = 0
    last_pos = len(a)-1
    flag = 0
    count=0

    while(first_pos<last_pos and flag==0):
        count+=1
        mid = (first_pos+last_pos)//2
        if(x==a[mid]):
            flag = 1
            print("Element found at position: ",mid)
            print("Number of iterations: ",count)
            return
        else:
            if(x<a[mid]):
                last_pos = mid-1
            else:
                first_pos = mid+1
    print("Element not found")