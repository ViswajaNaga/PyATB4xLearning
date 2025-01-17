# to read csv file

import pandas as pd

class Test_CRUD():

    def test_update_2(self):
        df=pd.read_csv('src/OCT/dt_10102024/userdata.csv')
        print(df)