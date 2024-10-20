import csv

class Test_CRUD():
    def test_update_1(self):
        with open('src/OCT/dt_10102024/userdata.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])


