import pandas as pd

data_dict = {"id":[],"minutes_active":[]}
df = pd.DataFrame(data_dict)
i = 0
for i in range(10):
    df["id"][i] = "id" + str(i)
    i += 1

df.loc["id1"]

