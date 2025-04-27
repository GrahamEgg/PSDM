import pandas as pd
from datetime import datetime


def receive_data(paths_list, date_bool, folder_location):
	result = []
	current_date = datetime.now().strftime("%m/%d/%Y")

	dfs = [pd.read_csv(pad) for pad in paths_list]
	
	

	amount_of_rows = len(dfs[0])

	for i in range(amount_of_rows):
		#print(i)
		opties = []

		for df in dfs:
			rij = df.iloc[i].to_dict()
			opties.append(rij)

		beste = max(opties, key=lambda x: x['Sex_cm'])
		
		result.append(beste)

	df_result = pd.DataFrame(result)

	df_clean = df_result.sort_values('Sex_cm', ascending=False).drop_duplicates('_Rec_id')
	#df_clean = df_result.sort_values(df_result['Sex_cm'].astype(str).str.len(), ascending=False).drop_duplicates('_Rec_id')

	df_clean = df_clean.sort_values('_Rec_id')

	# add date if empty
	if date_bool:
		df_clean = add_date(df_clean, current_date)

	else:
		print("Date will not be edited.")

	df_clean['Sex_cm'] = df_clean['Sex_cm'].astype('Int64')
	df_clean.to_csv(rf"{folder_location}_test_merger_DM.csv", index=True)




def add_date(df, date):
	print("add date")
	df.loc[
		df['Sex_cm'].between(0, 5) & df["Flw_dt"].isna(),
		'Flw_dt'
		] = date

	return df