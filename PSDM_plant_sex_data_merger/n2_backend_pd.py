import pandas as pd


def receive_data(paths_list, bool):
	print(paths_list)
	print(bool)
	result = []

	dfs = [pd.read_csv(pad) for pad in paths_list]

	amount_of_rows = len(dfs[0])

	for i in range(amount_of_rows):
		print(i)
		opties = []

		for df in dfs:
			rij = df.iloc[i].to_dict()
			opties.append(rij)

		beste = max(opties, key=lambda x: x['Sex_cm'])
		result.append(beste)

	#print(result)
	df_result = pd.DataFrame(result)

	df_clean = df_result.sort_values('Sex_cm', ascending=False).drop_duplicates('_Rec_id')
	df_clean = df_clean.sort_values('_Rec_id')

	#print(df_clean['_Rec_id'], df_clean['Sex_cm'])
