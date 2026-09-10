#Exercise 2.2
def sortarray(xs):
    # Menggunakan algoritma Bubble Sort sederhana
    arr = xs.copy() # copy array agar tidak mengubah data aslinya
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Tukar posisi jika elemen saat ini lebih besar dari elemen berikutnya
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

data = [5, 2, 8, 1, 9, 3]
t = sortarray(data)
print("Sorted array:", t)
