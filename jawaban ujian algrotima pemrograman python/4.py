def rerata_nilai_mhs(nama, dataDict):

    nilai_list = dataDict[nama]


    for nilai in nilai_list:
        print(nilai, end=" ")
    print()       

    rata2 = sum(nilai_list) / len(nilai_list)
    print("rata2 =", int(rata2))

dataDict = {
    'Icha': [80, 70, 70, 80]
}
rerata_nilai_mhs('Icha', dataDict)
