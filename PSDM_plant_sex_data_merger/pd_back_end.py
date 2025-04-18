import pandas as pd


def receive_data(paths_list, bool):
	print(paths_list)
	print(bool)

	dfs = [pd.read_csv(pad) for pad in paths_list]
	amount_of_rows = len(dfs[0])
	col_headers = list(dfs[0].columns.values)
	print(col_headers)
	result = []

	for i  in range(amount_of_rows):
		opties = []
		amount_of_headers = len(col_headers)
		for df in dfs:
			_FieldNrShort = df.iloc[i]['_FieldNrShort']
			_FieldNr = df.iloc[i]['_FieldNr']
			_PlantNr = df.iloc[i]['_PlantNr']
			_Rec_id = df.iloc[i]['_Rec_id']
			iv_id = df.iloc[i]['iv_id']
			Flw_dt = df.iloc[i]['Flw_dt']
			Sex_cm = df.iloc[i]['Sex_cm']
			SexRev_dt = df.iloc[i]['SexRev_dt']
			SSet_dt = df.iloc[i]['SSet_dt']
			_PlotComments = df.iloc[i]['_PlotComments']
			_pi_pd_SubLocation = df.iloc[i]['_pi_pd_SubLocation']
			_WhoObserved = df.iloc[i]['_WhoObserved']
			GrowerName = df.iloc[i]['GrowerName']
			GrowerLocation = df.iloc[i]['GrowerLocation']
			_DateObserved = df.iloc[i]['_DateObserved']
			_HarvestNr = df.iloc[i]['_HarvestNr']
			_DateHarvested = df.iloc[i]['_DateHarvested']
			_ObservationNr = df.iloc[i]['_ObservationNr']
			_BookComments = df.iloc[i]['_BookComments']
			GCEntryID = df.iloc[i]['GCEntryID']
			GCExportID = df.iloc[i]['GCExportID']
			opties.append((_FieldNrShort, _FieldNr, _PlantNr,_Rec_id,iv_id, Flw_dt,Sex_cm,SexRev_dt,SSet_dt,
			               _PlotComments,_pi_pd_SubLocation,_WhoObserved,GrowerName,GrowerLocation,_DateObserved,
			               _HarvestNr,_DateHarvested,_ObservationNr,_BookComments,GCEntryID,GCExportID))

			beste = max(opties, key=lambda x: x[6])


			result.append({
				'_FieldNrShort': beste[0],
				'_FieldNr': beste[1],
				'_PlantNr': beste[2],
				'_Rec_id': beste[3],
				'iv_id': beste[4],
				'Flw_dt': beste[5],
				'Sex_cm': beste[6],
				'SexRev_dt': beste[7],
				'SSet_dt': beste[8],
				'_PlotComments': beste[9],
				'_pi_pd_SubLocation': beste[10],
				'_WhoObserved': beste[11],
				'GrowerName': beste[12],
				'GrowerLocation': beste[13],
				'_DateObserved': beste[14],
				'_HarvestNr': beste[15],
				'_DateHarvested': beste[16],
				'_ObservationNr': beste[17],
				'_BookComments': beste[18],
				'GCEntryID': beste[19],
				'GCExportID': beste[20]
				}
			)
	df_result = pd.DataFrame(result)
	df_clean = df_result.sort_values('Sex_cm',ascending=False).drop_duplicates('_Rec_id')
	df_clean = df_clean.sort_values('_Rec_id')

	print(df_clean['_Rec_id'],df_clean['Sex_cm'])






