def Conversion(array):
    l = array.split(',')
    for i in range(len(l)):
        for i in range(len(l)):
            l[i] = int(l[i])
    return l

def SelectionSort(array):
    final_list = []
    l = Conversion(array)
    for i in range(len(l)):
        final_list.append(l.copy())
        min = i
        for j in range(i + 1, len(l)):
            if l[min] > l[j]:
                min = j
        l[i], l[min] = l[min], l[i]
    return final_list, len(final_list[0])