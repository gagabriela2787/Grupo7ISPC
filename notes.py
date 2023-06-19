import csv

notes = ''
with open('nacidos-vivos-registrados-2018_deis.csv', newline='') as f:
    data = csv.reader(f, delimiter=',')
    notes= list(data)


#print(notes)


def getData(notes):
    for i in range(1,len(notes)):
        for j in range(len(notes[i])):
            print(notes[0][j] + ':' + notes[i][j])
        print('')
        
getData(notes)
