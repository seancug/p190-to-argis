import string

def Transform(file_name):
    fp = open(file_name, 'r')
    read_all = fp.readlines()

    all_lines = []
    totalline = 0
    for i in range(57, len(read_all) -1):
        line_name = read_all[i][0:10]
        shot_num = read_all[i][21:25]
        du = string.atof(read_all[i][25:27])
        fen = string.atof(read_all[i][27:29])
        miao = string.atof(read_all[i][29:34])
        latitude = du + fen / 60.0 + miao / 3600.0

        du1 = string.atof(read_all[i][35:38])
        fen1 = string.atof(read_all[i][38:40])
        miao1 = string.atof(read_all[i][40:45])
        longitude = du1 + fen1 / 60.0 + miao1 / 3600.0
        all_lines.append(line_name + "\t" + shot_num + "\t" + str(latitude) + "\t" + str(longitude) + "\n")
        totalline += 1
    fp.close()
    print "Finished Transformed\t" + file_name + "\ntotal lines:\t" + str(totalline)
    print ''
    return all_lines