


"""
1. Given a list of numbers, find the GCF  -->  [12,36,72] 

2. Find the number that is repeating the most in the given set -->  [0,0,3,4,5,4,4,4 ] 

3. Find the sum of all the multiples of 3 or 5 below 1000.
"""

def array_sort(inarray):
    outarray=[]
    while inarray:
        minimum=inarray[0]
        for k in inarray:
            if k<minimum:
                minimum=k
        outarray.append(minimum)
        inarray.remove(minimum)
    return outarray


def find_gcf(inarray):
    sorted_inarray=array_sort(inarray)
    gcf_element_sum=[]
    for k in sorted_inarray:
        gcf_element_sum.append(sum([element%k for element in sorted_inarray]))
    print gcf_element_sum
    find_divisible=[1 if n==0 else 0 for n in gcf_element_sum]
    gcf=sorted_inarray[find_divisible.index(1)]
    return gcf

def find_mode(inarray):
    sorted_inarray=array_sort(inarray)
    curr_element_ct=[]
    for curr_element in sorted_inarray:
        curr_element_ct.append(sum([1 if k==curr_element else 0 for k in sorted_inarray]))
    mode_idx=curr_element_ct.index(max(curr_element_ct))
    return sorted_inarray.pop(mode_idx)

def find_3_5_mulitple_sum(num,fact1=3,fact2=5):
    list1000=range(num)
    divisible_3_5=[q if (q%fact1==0) or (q%fact2==0) else 0 for q in list1000]
    return sum(divisible_3_5)



