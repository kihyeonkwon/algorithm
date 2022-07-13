data_dict = {"TV": 2000000,

"냉장고": 1500000,

"책상": 350000,

"노트북": 1200000,

"가스레인지": 200000,

"세탁기": 1000000}


b=sorted(data_dict.values(), reverse=True)


for i in b:
    for j in data_dict:
        if data_dict[j]==i:
            print( "{0}: {1}".format(j, i))