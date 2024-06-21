def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def pyramid_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
if __name__ == "__main__":
    data = []
    while True:
        try:
            num = input("Enter a number (or 'q' to qui
            if num.lower() == 'q':
                break
            data.append(int(num))
        except ValueError:
            print("Invalid input. Please enter a numbe
    pyramid_sort(data)
    print("Sorted data:", data)