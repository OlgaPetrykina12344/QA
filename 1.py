def max_number(array):
    result=0
    for element in array:
        if result<element:
            result=element
    return result

def min_number(array):
    result=10**10
    for element in array:
        if result>element:
            result=element
    return result

def sort_array(array):
    pivot = arr[ler(array)//2]
    middle = [element for element in array if element == pivot]
    right = [element for element in array if element > pivot]
    return sort_array(left) + middle + sort_array(right)
n=input()
array=list(int(i) for i in n.replace(',','').split())
print(f"""
Четные числа: {[x for x in array if x % 2 == 0]}
Максимальное число: {max(array)}
Минимальное число: {min(array)}
Отсортированный список : {sorted(array)}
""")