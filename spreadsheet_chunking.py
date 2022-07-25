import pandas as pd
 
f="data_file"
source_path = "/home/robby/Documents/code_testing/data_file.csv"

for i,chunk in enumerate(pd.read_csv(source_path, chunksize=30000)):
    chunk.to_csv(f"/home/robby/Documents/code_testing/{f}_migrate_update_case_{i}.csv", index=False)
