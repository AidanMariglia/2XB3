
#bottom up mergesort adapted from sedgewick wayne
def mergesort_bottom(L):
    n = len(L)

    length = 1

    while(length < n):
        low = 0
        while(low < n - length):
            merge_bottom(L, low, low + length - 1, \
            min(low + 2 * length - 1, n - 1))
            low += 2*length
        length *= 2



#inplace merge adapted from sedgewick wayne
def merge_bottom(L, start, mid, end):
    i = 0
    j = (mid + 1) - start
    aux = []
    #copy to aux array   
    for k in range(start, end + 1):
        aux.append(L[k])

    for k in range(start, end + 1):
        if   (i > (mid- start)):         L[k] = aux[j]; j += 1
        elif (j > (end - start)):         L[k] = aux[i]; i += 1
        elif (aux[j] < aux[i]): L[k] = aux[j]; j += 1
        else :                  L[k] = aux[i]; i += 1


def main():
    test = [4,5,6,1,3,4]

    mergesort_bottom(test)

    print(test)

main()

