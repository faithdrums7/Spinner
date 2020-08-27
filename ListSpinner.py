#nomor 2
# listAwal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# listOutput = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

def CounterClockWise(listAwal):
    data_mutar = [[], [], []]                                            #kita buat list kosong yang berisi 3 list kosong 
    for i in range(len(listAwal)):                                       # karena dimensi list 3x3 maka i dan jnya juga 3 dan 3
        for j in range(len(listAwal)):
            data_mutar[i].append(listAwal[(j)][(len(listAwal)-1)-i])     # fungsi append untuk menambahkan value pada index tertentu ke dalam suatu list
    return data_mutar

# len(listAwal) = 3
# karena in RANGE maka i dan j akan maksimal di index 2
# Loop pertama i = 0 j = 0
# data_mutar[i].append(listAwal[(j)][(len(listAwal)-1)-i])
# data_mutar[0].append(yourList[0][3-1-0])
# data_mutar[0].append(yourList[0][2])

# Loop kedua i = 0 j = 1
# data_mutar[0].append(yourList[1][3-1-0])
# data_mutar[0].append(yourList[1][2]) == value pada index listAwal[1][2] kita masukkan ke list data_mutar

# Loop ketiga i = 0 j = 2
# data_mutar[0].append(yourList[2][3-1-0])
# data_mutar[0].append(yourList[2][2])
# []

# setelah loop ketiga maka i akan menjadi 1
# loop keempat i = 1 j = 0
# dan loop seterusnya........

# data_mutar        listAwal
# [[], [], []}	  [[1,  2,  3],  [4,  5,  6],    [7,  8,  9]]
#   0   1   2      0,1 0,2  0,3   1,0 1,1 1,2    2,0 2,1 2,2
# listOutput =    [[3,  6,  9],  [2,   5,   8],  [1,  4,  7]]
#                   0,2 1,2 2,2   0,1  1,1 ,2,1  0,0  1,0  2,0

listAwal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(CounterClockWise(listAwal))