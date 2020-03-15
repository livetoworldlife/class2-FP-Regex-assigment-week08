# Write the following city names sequentially to the file “sehir.txt” with plate sign belong to each.
cities = ['Icel','Istanbul', 'Izmir','Kars', 'Kastamonu', 'Kayseri', 'Kirklareli', 'Kirsehir', 'Kocaeli','Konya']
plates = [33,34,35,36,37,38,39,40,41,42]

with open("sehir.txt","w+") as f:
    for i, j in zip(cities,plates):
        f.write("Plate Sing of %s: " % i + "%d\n" % j )
    


