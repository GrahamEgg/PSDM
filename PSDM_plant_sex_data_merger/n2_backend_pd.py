import pandas as pd
from datetime import datetime
import os



def receive_data(paths_list, date_bool, folder_location):
	result = []
	current_date = datetime.now().strftime("%m/%d/%Y")
	current_date_for_file_name = datetime.now().strftime("%m-%d-%Y")
	dfs = [pd.read_csv(pad) for pad in paths_list]
	
	df_combind = pd.concat(dfs)
	#print(df_combind)
	df_clean = df_combind.sort_values('Sex_cm', ascending=False).drop_duplicates('_Rec_id')
	#df_clean = df_result.sort_values(df_result['Sex_cm'].astype(str).str.len(), ascending=False).drop_duplicates('_Rec_id')
	#print(df_clean[['_Rec_id', 'Sex_cm']])
	df_clean = df_clean.sort_values('_Rec_id')

	# add date if empty
	if date_bool:
		df_clean = add_date(df_clean, current_date)

	else:
		print("Date will not be edited.")
	 
	df_clean['Sex_cm'] = df_clean['Sex_cm'].astype('Int64')
	
	path = os.path.join(folder_location, f"plant_sex_data_merge_{current_date_for_file_name}_DM.csv")
	df_clean.to_csv(path, index=True)




def add_date(df, date):
	print("add date")
	df.loc[
		df['Sex_cm'].between(0, 6) & df["Flw_dt"].isna(),
		'Flw_dt'
		] = date

	return df