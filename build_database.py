# import csv
# import json
import math
# import operator

# deltas = {}
# connections = {}

def sigmasoid(x):
	return 1 if x > 0 else -1
	return 2 / (1 + math.e**(-3*x)) - 1

# ############ get all the dataset names
# from os import listdir
# from os.path import isfile, join
# csvs = ["datasets/training/"+f for f in listdir("datasets/training") if isfile(join("datasets/training", f)) and '.csv' in f]
# ########### print it
# # print csvs
# ##############


# ########### build the datasets in memory
# for csv_file_name in csvs:
# 	deltas[csv_file_name] = {}
# 	last_price = None
# 	with open(csv_file_name, 'r') as f:
# 	    reader = csv.reader(f)
# 	    for line in reader:
# 	    	if "201" in line[0]:
# 	    		current_price = float(line[4])
# 	    		if last_price != None:
# 	    			deltas[csv_file_name][line[0]] = 1 if (current_price / float(last_price) > 1.01) else -1 if (current_price / float(last_price) < .99) else 0#(current_price/last_price)-1.0
# 	    		last_price = current_price

# # subtract the average from each value
# # for csv_file_name in csvs:
# # 	average = float(sum(deltas[csv_file_name].values())) / len(deltas[csv_file_name].values())
# # 	for date in deltas[csv_file_name].keys():
# # 		deltas[csv_file_name][date] = (deltas[csv_file_name][date]-average)
# ########### print it
# # print json.dumps(deltas)
# ############################






# ########### build the connections
# for csv_file_name1 in csvs:
# 	connections[csv_file_name1.replace("datasets/training/", "")] = {}
# 	for csv_file_name2 in csvs:
# 		if csv_file_name1 != csv_file_name2:
# 			try:
# 				connections[csv_file_name1.replace("datasets/training/", "")][csv_file_name2.replace("datasets/training/", "")] = sum([    (deltas[csv_file_name1][date]*deltas[csv_file_name2][date])   for date in deltas[csv_file_name1].keys()]) / float(len(deltas[csv_file_name1].keys()))
# 			except:
# 				pass
# ####### print it
# # print json.dumps(connections)
# #######################





# ############ write to the file
# with open("connections.txt", "w") as file:
# 	for c in connections.keys():
# 		file.write(c.replace("datasets/", "") + " ")
# 	for c in connections.keys():
# 		file.write("\n")
# 		for k in connections.keys():
# 			file.write(str(connections[c].get(k, "Null")) + " ")
# #############



# # def test(input_vals):
# # 	new_deltas = {}
# # 	for key in input_vals.keys():
# # 		try:
# # 			new_deltas[key] = sigmasoid(sum([input_vals[k]*connections[k][key] for k in connections[key].keys() if abs(connections[k][key]) > 0.5]))
# # 		except:
# # 			pass
# # 	for i in range(0):
# # 		for key in input_vals.keys():
# # 			try:
# # 				new_deltas[key] = sigmasoid(sum([new_deltas[k]*connections[key][k] for k in connections[key].keys() if abs(connections[k][key]) > 0.5]))
# # 			except:
# # 				pass
# # 	return new_deltas

# # validation_csvs = ["datasets/validation/"+f for f in listdir("datasets/validation") if isfile(join("datasets/validation", f)) and '.csv' in f]
# # validated = {}
# # for f in validation_csvs:
# # 	with open(f, "r") as file:
# # 		last = None
# # 		reader = csv.reader(file)
# # 		for line in reader:
# # 			if "2016" in line[0] and last == None:
# # 				last = float(line[4])
# # 			elif "2016" in line[0]:
# # 				validated[f.replace("datasets/validation/", "")] = 1 if (current_price / float(last) > 1.01) else -1 if (current_price / float(last) < .99) else 0

# # print validated

# def copy(dict1):
# 	new_dict = {}
# 	for key in dict1.keys():
# 		new_dict[key] = dict1[key]
# 	return new_dict

# def diffuse(initial_name):

# 	# set up initial values
# 	# everything is 0 except for the value for the initial_name
# 	old_values = {}
# 	for key in connections.keys():
# 		old_values[key] = 0
# 	old_values[initial_name] = 1.0

# 	new_values = copy(old_values)

# 	for iteration in range(12):
# 		print iteration
# 		for key in old_values.keys():
# 			for con in connections[key].keys():
# 				new_values[con] += old_values[key]*connections[key][con] / len(connections.keys())

# 		for key in new_values.keys():
# 			new_values[key] = sigmasoid(new_values[key])
# 		old_values = copy(new_values)

# 	# print new_values



	
# diffuse("XOM.csv")

# pick a random day and show everything for that
# 2012-03-15
# validation_data = {}
# for name in deltas.keys():
# 	validation_data[name] = deltas[name]["2012-03-15"]
# print validation_data

guesses = {'MCO.csv': 0.8242748146967347, 'ACN.csv': 0.813563288192827, 'SO.csv': 0.5699601605849309, 'CSCO.csv': 0.7627116123240216, 'CERN.csv': 0.7289944335372205, 'AMZN.csv': 0.7284133140260485, 'KEY.csv': 0.8201544857850367, 'DFS.csv': 0.8034380820652545, 'LOW.csv': 0.7550520128206331, 'CPB.csv': 0.6451410471324641, 'SCHW.csv': 0.804143154288496, 'AVY.csv': 0.8142334138299085, 'FISV.csv': 0.831114923634305, 'JWN.csv': 0.738382779442972, 'ED.csv': 0.4879999500304064, 'DPS.csv': 0.6172156587288182, 'ESRX.csv': 0.6738589278990901, 'DISH.csv': 0.7075279609069474, 'CELG.csv': 0.6546742864726642, 'TXT.csv': 0.8428620805725513, 'HST.csv': 0.8156192116136876, 'STX.csv': 0.7393262092716573, 'HCN.csv': 0.56485377016668, 'NEM.csv': 0.33647706493299334, 'DG.csv': 0.5472930612997087, 'GIS.csv': 0.6093860770752062, 'SHW.csv': 0.7834215170155998, 'SYMC.csv': 0.7486757990478494, 'DISCA.csv': 0.79141611347796, 'APA.csv': 0.7795760533007192, 'GS.csv': 0.8395555997030506, 'PCLN.csv': 0.7214540805126362, 'NDAQ.csv': 0.808382375895565, 'BP.csv': 0.8136377600782059, 'CME.csv': 0.7088464671515164, 'LEG.csv': 0.8107920814118956, 'CMS.csv': 0.6505212748175107, 'SWK.csv': 0.8209134971368688, 'AIG.csv': 0.8337005603453227, 'ULTA.csv': 0.6285660233562718, 'AMP.csv': 0.8668872889753501, 'MET.csv': 0.8381983145213705, 'MAR.csv': 0.8225609324454468, 'ORCL.csv': 0.8253198067596856, 'EBAY.csv': 0.6118607404725329, 'XEL.csv': 0.6548816985431669, 'EQR.csv': 0.6370222132580514, 'HSIC.csv': 0.8160701742230971, 'CMI.csv': 0.8419020327089588, 'GM.csv': 0.8030642886958337, 'VTR.csv': 0.558934618801133, 'VFC.csv': 0.7707329324074998, 'UNH.csv': 0.6640718018238065, 'TRV.csv': 0.8034740852486317, 'KIM.csv': 0.7600180396619549, 'FCX.csv': 0.7530703535868926, 'FMC.csv': 0.8016787620480708, 'GRMN.csv': 0.7781955020161608, 'HRS.csv': 0.7966560839133339, 'TSS.csv': 0.8023129647231644, 'DOV.csv': 0.8314050527079115, 'AMGN.csv': 0.7513616422233533, 'AXP.csv': 0.8209236305161296, 'DTE.csv': 0.6839323775747854, 'UAL.csv': 0.6913371075615753, 'STI.csv': 0.8322957196298741, 'LLY.csv': 0.6631065436740708, 'HBAN.csv': 0.8108764244865865, 'BXP.csv': 0.7573952095168572, 'AVB.csv': 0.6474054863114849, 'IBM.csv': 0.7602891761755324, 'YUM.csv': 0.7617563336486979, 'RF.csv': 0.8203184218139221, 'INTU.csv': 0.7704355017513507, 'LH.csv': 0.7233796739272105, 'LRCX.csv': 0.7946663577636144, 'JBHT.csv': 0.7648564512852227, 'ROP.csv': 0.7998274190741415, 'LNT.csv': 0.7050647752203261, 'CTXS.csv': 0.7413889011362111, 'RL.csv': 0.7627407848230889, 'WMT.csv': 0.6382460678741462, 'IDXX.csv': 0.7193626755835145, 'MAS.csv': 0.8096848896503457, 'SIG.csv': 0.7331006133025895, 'F.csv': 0.8318976193916348, 'JPM.csv': 0.8171832713888889, 'WYN.csv': 0.8072678954682917, 'KSU.csv': 0.8232182216869981, 'SNA.csv': 0.8257270305797131, 'CAG.csv': 0.6859434039129948, 'AES.csv': 0.8033452812182704, 'PGR.csv': 0.7531506896270075, 'MTD.csv': 0.8141037130848621, 'LLL.csv': 0.816503151647292, 'AIZ.csv': 0.8053652876356445, 'PHM.csv': 0.8034957476087075, 'URI.csv': 0.8201269248325966, 'GLW.csv': 0.8110870593710482, 'MAC.csv': 0.7316041576899142, 'CA.csv': 0.8170019002428188, 'CNC.csv': 0.633438411507284, 'TIF.csv': 0.7325889046182785, 'XRAY.csv': 0.8192738041086631, 'CTSH.csv': 0.7535091690856761, 'INCY.csv': 0.598016212865577, 'SRE.csv': 0.7545912777200083, 'WM.csv': 0.7572681567437851, 'BLL.csv': 0.7828830226311283, 'AOS.csv': 0.8265668469996141, 'ALXN.csv': 0.7130695631223656, 'UTX.csv': 0.8451442859304161, 'LEN.csv': 0.7620879005310504, 'DISCK.csv': 0.7350169686198074, 'MU.csv': 0.7137896973376023, 'CBS.csv': 0.7980866212486311, 'DVA.csv': 0.6707932118450763, 'EA.csv': 0.6812558349670612, 'LYB.csv': 0.7660875410797894, 'SPGI.csv': 0.7841335408262042, 'FFIV.csv': 0.7354867508567273, 'OKE.csv': 0.7680360196286695, 'BCR.csv': 0.7071797307248835, 'XOM.csv': 0.9114373541998728, 'GILD.csv': 0.7936328651961926, 'NVDA.csv': 0.7381165352979635, 'MS.csv': 0.8224230119697304, 'AME.csv': 0.8440989414037738, 'BLK.csv': 0.8638557039080521, 'IFF.csv': 0.8034773615101676, 'CHD.csv': 0.6132264352952297, 'COST.csv': 0.6612139484051867, 'NTAP.csv': 0.7116142584688327, 'ALL.csv': 0.8030962380048814, 'FE.csv': 0.5841142597936311, 'ALGN.csv': 0.7313326676508809, 'INTC.csv': 0.7785314340675271, 'EMN.csv': 0.8363804724515813, 'M.csv': 0.7525247498284118, 'JEC.csv': 0.8379308368772587, 'DHI.csv': 0.766364921725404, 'SEE.csv': 0.8138652437641747, '_oil.csv': 0.0, 'CB.csv': 0.7928148210876462, 'JNPR.csv': 0.764876449783136, 'TMO.csv': 0.7947916887502862, 'ATVI.csv': 0.7227094219643682, 'CBOE.csv': 0.6238201297563288, 'PPG.csv': 0.8353166032910826, 'ADBE.csv': 0.7816178679938963, 'KSS.csv': 0.6496077695194877, 'UAA.csv': 0.6644105871104617, 'BF.B.csv': 0.7558120336902123, 'STT.csv': 0.8346909878303197, 'TROW.csv': 0.8601596404029446, 'RRC.csv': 0.6328202425977927, 'MO.csv': 0.6351209633621973, 'HES.csv': 0.8129442412840215, 'BWA.csv': 0.8362924387133766, 'NFX.csv': 0.7972028118979759, 'LNC.csv': 0.859095590689775, 'OXY.csv': 0.8001859676901877, 'FOX.csv': 0.8049898027850464, 'UNM.csv': 0.8338234280723673, 'PAYX.csv': 0.7933474796976059, 'FDX.csv': 0.8061427439376516, 'ROST.csv': 0.7029030980734707, 'TMK.csv': 0.8101186763653299, 'FITB.csv': 0.7785798398069581, 'VRTX.csv': 0.629749649898862, 'IP.csv': 0.7977801122892394, 'BMY.csv': 0.6261716473376497, 'COL.csv': 0.8202979045059526, 'WMB.csv': 0.7616467209073128, 'KMI.csv': 0.7416714026686537, 'V.csv': 0.8040494327993455, 'GOOGL.csv': 0.7266153508131714, 'LUV.csv': 0.7356791243308907, 'ILMN.csv': 0.6775720728414396, 'CINF.csv': 0.8105871658634816, 'EW.csv': 0.5885851810908946, 'TWX.csv': 0.7967757899036085, 'TXN.csv': 0.827080058029581, 'PTR.csv': 0.7396037453809896, 'MON.csv': 0.7765823870503741, 'VLO.csv': 0.736724876015322, 'MTB.csv': 0.7914873653005616, 'MAA.csv': 0.5851687908456606, 'EMR.csv': 0.8372092380734604, 'CF.csv': 0.7094137879812834, 'DHR.csv': 0.8192870356755557, 'ETFC.csv': 0.7877628267918357, 'PWR.csv': 0.8192054060700569, 'COH.csv': 0.7261595839349919, 'AIV.csv': 0.6339169771985582, 'DE.csv': 0.7439506663081719, 'ZION.csv': 0.8018211546119718, 'HRL.csv': 0.7313126409466431, 'ABC.csv': 0.6420353399370857, 'WLTW.csv': 0.7633289579208637, 'NKE.csv': 0.7294352984234138, 'ALB.csv': 0.8059278573049267, 'VRSK.csv': 0.7617958389983239, 'PKG.csv': 0.823561404772583, 'AZO.csv': 0.6146806297463006, 'ANDV.csv': 0.6965025056311658, 'EQT.csv': 0.7625954091101881, 'MMC.csv': 0.8293085972836844, 'NUE.csv': 0.8184917603848838, 'EXC.csv': 0.5839891841570803, 'NOV.csv': 0.751232845606304, 'MPC.csv': 0.7191191427355073, 'T.csv': 0.7190923474682172, 'APH.csv': 0.8396188622357663, 'XEC.csv': 0.7269181537688811, 'PKI.csv': 0.8269604647298499, 'BBT.csv': 0.8174414598024768, 'JNJ.csv': 0.7490783901998834, 'ORLY.csv': 0.6692409702094171, 'RSG.csv': 0.7654670354326756, 'D.csv': 0.6473862529049748, 'VRSN.csv': 0.7171217742777545, 'XLNX.csv': 0.7883650855816664, 'COF.csv': 0.80978467193458, 'IT.csv': 0.752944592221217, 'VNO.csv': 0.7576231742242858, 'AKAM.csv': 0.7617538823320515, 'ANTM.csv': 0.6742352421422044, 'ETR.csv': 0.5951408541216823, 'BAC.csv': 0.7776469881151433, 'DLR.csv': 0.5601605241199057, 'CL.csv': 0.7295605905165277, 'DRI.csv': 0.6487597600111314, 'AWK.csv': 0.6106369166075927, 'RCL.csv': 0.7842319489427576, 'MAT.csv': 0.790826832155066, 'ISRG.csv': 0.6684838971838283, 'MKC.csv': 0.7096598066942905, 'RTN.csv': 0.8075109530248776, 'SCG.csv': 0.703255514160338, 'BRK.B.csv': 0.8274287741278925, 'AET.csv': 0.7065961540619439, 'ANSS.csv': 0.7711671501529946, 'TEL.csv': 0.8395344342112583, 'BK.csv': 0.8364971206135252, 'AFL.csv': 0.8116672364291884, 'EL.csv': 0.7693510413067701, 'HCP.csv': 0.5561895884202124, 'SLG.csv': 0.774791556837225, 'KLAC.csv': 0.7914349966593897, 'HAL.csv': 0.7882775923573613, 'TJX.csv': 0.7461275133073018, 'ARE.csv': 0.7211131899695353, 'ROK.csv': 0.8346063030412605, 'HRB.csv': 0.6926276160476279, 'PM.csv': 0.6852590626487862, 'MMM.csv': 0.8458893165991688, 'DGX.csv': 0.691382353475219, 'HP.csv': 0.7967976953661695, 'FLR.csv': 0.8452532810656042, 'BIIB.csv': 0.7228610012233541, 'PG.csv': 0.6821869207438831, 'MA.csv': 0.8302459538411007, 'CBG.csv': 0.8200508282563141, 'HIG.csv': 0.8311563756622038, 'VIAB.csv': 0.7447831155219986, 'CAH.csv': 0.7607439275781547, 'HBI.csv': 0.772075378451361, 'BA.csv': 0.8045940669499887, 'PNW.csv': 0.7329762629290373, 'ECL.csv': 0.8230034541374189, 'NI.csv': 0.7639075561388589, 'WY.csv': 0.8054487362442813, 'APD.csv': 0.8286400954811504, 'HSY.csv': 0.6753796337479361, 'PRU.csv': 0.8250319245760118, 'KMB.csv': 0.6661416720213695, 'PNC.csv': 0.8208097720467338, 'SJM.csv': 0.7217904894708509, 'AEP.csv': 0.7142405189222882, 'ZBH.csv': 0.8106851051849231, 'UNP.csv': 0.8376753306817919, 'CSX.csv': 0.8124201826259121, 'WYNN.csv': 0.6214208733069659, 'HAS.csv': 0.7349797418749078, 'RE.csv': 0.7433837092397022, 'BBY.csv': 0.6374060351702291, 'ARNC.csv': 0.8022150326432478, 'GWW.csv': 0.7861186580592601, 'FRT.csv': 0.6682790848164335, 'AAPL.csv': 0.6832443715722949, 'ES.csv': 0.6575776063744705, 'MHK.csv': 0.7958686095500669, 'O.csv': 0.6183837451159788, 'PLD.csv': 0.7903942703889277, 'NEE.csv': 0.6802006283765587, 'DUK.csv': 0.5970859807422269, 'EXPE.csv': 0.7763618353689468, 'LUK.csv': 0.7894097364769213, 'ALK.csv': 0.7043050656393595, 'COG.csv': 0.6338325769129238, 'HON.csv': 0.8376399395329786, 'GOOG.csv': 0.7178572126030665, 'PVH.csv': 0.739393380279064, 'PFG.csv': 0.8665626347212902, 'CTL.csv': 0.7183121330192648, 'SPLS.csv': 0.6941851365979572, 'CRM.csv': 0.7708462563511502, 'PH.csv': 0.8600855778637249, 'PBCT.csv': 0.7729629024968399, 'COP.csv': 0.8085017301717579, 'WHR.csv': 0.8181152890130208, 'PPL.csv': 0.6822495262525115, 'TAP.csv': 0.7128536243140333, 'FAST.csv': 0.7475707813570216, 'NFLX.csv': 0.5288844126964529, 'HOLX.csv': 0.7188626131898945, 'A.csv': 0.8265761412854769, 'CMG.csv': 0.6429656861372284, 'L.csv': 0.8186304023302895, 'EXR.csv': 0.6403498327826502, 'RHI.csv': 0.8177803938104693, 'REGN.csv': 0.5794768196929341, 'PFE.csv': 0.6820877923437905, 'MCHP.csv': 0.8073708919711156, 'STZ.csv': 0.7225656776340237, 'MGM.csv': 0.7847190125901704, 'KMX.csv': 0.7921313474595919, 'ABT.csv': 0.7574048849660497, 'PEP.csv': 0.6476709011720656, 'SYK.csv': 0.8191339590954863, 'WEC.csv': 0.6208402387430101, 'EXPD.csv': 0.7949521245097118, 'CVX.csv': 0.8326022396998412, 'RHT.csv': 0.773190482237111, 'WAT.csv': 0.7899006437153284, 'GE.csv': 0.7961955939423109, 'APC.csv': 0.8161332545320195, 'MCD.csv': 0.5966428271416626, 'UDR.csv': 0.5836856227392975, 'VAR.csv': 0.7391894322573451, 'AJG.csv': 0.8101877842892917, 'AEE.csv': 0.6469351107113086, 'PCAR.csv': 0.8584625163007285, 'FLIR.csv': 0.7627480602081638, 'AAP.csv': 0.66278410263062, 'DLTR.csv': 0.6317795440442366, 'DRE.csv': 0.7609910832176565, 'ADP.csv': 0.8321591820668197, 'IPG.csv': 0.8382956763674116, 'NRG.csv': 0.7092395218369572, 'K.csv': 0.6932355933293362, 'CAT.csv': 0.7963245674725341, 'PX.csv': 0.8083421590449416, 'TDG.csv': 0.7514341219655136, 'DIS.csv': 0.7961344756756563, 'WFC.csv': 0.8231854092712363, 'MOS.csv': 0.7583892541008004, 'BSX.csv': 0.7867845860676734, 'C.csv': 0.8224278845692112, 'EFX.csv': 0.7820555682354253, 'CTAS.csv': 0.8006737085997713, 'DVN.csv': 0.8030506382063782, 'ENB.csv': 0.7490644286921417, 'VZ.csv': 0.708988652683431, 'HCA.csv': 0.6823197124350739, 'CVS.csv': 0.7504555683592746, 'GPS.csv': 0.7335506308767417, 'FOXA.csv': 0.8063854500498222, 'KR.csv': 0.7183049789115434, 'HOG.csv': 0.8218902489504407, 'BDX.csv': 0.8036416399905157, 'COO.csv': 0.7147109670869993, 'CMCSA.csv': 0.8012431321410449, 'CNP.csv': 0.7479503465999102, 'CHRW.csv': 0.6794873314610343, 'GD.csv': 0.8432122674433145, 'EOG.csv': 0.8202481793494134, 'QCOM.csv': 0.7258072179571156, 'TSCO.csv': 0.7485594079644491, 'MCK.csv': 0.7569836182652576, 'PCG.csv': 0.5888717350430046, 'CMA.csv': 0.8230882255272012, 'CHK.csv': 0.7455380441423196, 'XRX.csv': 0.7792946974044905, 'KO.csv': 0.6778234609059601, 'VMC.csv': 0.8004536528795141, 'PXD.csv': 0.7755642450902618, 'HUM.csv': 0.6419208598582715, 'AYI.csv': 0.8245698048804435, 'SBUX.csv': 0.7132319553141535, 'ADSK.csv': 0.7889927859463415, 'MLM.csv': 0.7609014108443748, 'ITW.csv': 0.8433049038999592, 'AMG.csv': 0.8672584151543161, 'PSA.csv': 0.6206458010039975, 'FIS.csv': 0.7840721323466797, 'NOC.csv': 0.822206495278158, 'CI.csv': 0.6753260626515936, 'CXO.csv': 0.7799711237499076, 'PEG.csv': 0.6474332238588352, 'BEN.csv': 0.8503377781749564, 'NSC.csv': 0.8209515798257292, 'RJF.csv': 0.8356628626105052, 'HD.csv': 0.7685689243657605, 'LKQ.csv': 0.7492802279206097, 'CLX.csv': 0.5589343248360805, 'USB.csv': 0.8326018693171677, 'SYY.csv': 0.6640616042052774, 'RMD.csv': 0.6730624493693502, 'FL.csv': 0.6907930286978281, 'REG.csv': 0.7382420711412738, 'HPQ.csv': 0.6845567805690844, 'IR.csv': 0.8281242310547641, 'PDCO.csv': 0.7725952953906257, 'WDC.csv': 0.7617295151055135, 'SPG.csv': 0.7147756619352454, 'GGP.csv': 0.6755806851712134, 'GPC.csv': 0.8312970568031779, 'OMC.csv': 0.827058679121973, 'UHS.csv': 0.7407988815146103, 'MSFT.csv': 0.7825768001352347, 'ADS.csv': 0.7571172033824323, 'DAL.csv': 0.7182796338255097, 'SU.csv': 0.809664514277272, 'TSN.csv': 0.6538358306810745, 'UPS.csv': 0.8276138572438934, 'AMD.csv': 0.7260438800655589, 'SWKS.csv': 0.7556332343498258, 'MSI.csv': 0.7080770013879563, 'SRCL.csv': 0.687759547564899, 'MRK.csv': 0.7214232760719026, 'FLS.csv': 0.8558345313402764, 'EIX.csv': 0.6229556294193521, 'BAX.csv': 0.7701800673741994, 'IVZ.csv': 0.8521749199193853, 'GPN.csv': 0.8055068558741538, 'ADM.csv': 0.7842827720417951, 'LB.csv': 0.68982433361348, 'MRO.csv': 0.8151724702146022, 'ESS.csv': 0.6514096796489013}

true = {'MSFT.csv': 1, 'COH.csv': 1, 'JNPR.csv': 0, 'AYI.csv': 1, 'UNP.csv': 1, 'IVZ.csv': 1, 'CSX.csv': 1, 'VLO.csv': 0, 'EA.csv': -1, 'JNJ.csv': 0, 'CBG.csv': 1, 'ULTA.csv': 1, 'GILD.csv': 1, 'GIS.csv': 0, 'ALB.csv': 1, 'ADP.csv': 1, 'EFX.csv': 1, 'CERN.csv': 1, 'VMC.csv': 1, 'HCN.csv': 0, 'CBOE.csv': 1, 'ATVI.csv': 1, 'AJG.csv': 1, 'MA.csv': 0, 'PHM.csv': 1, 'EOG.csv': 1, 'CTAS.csv': 1, 'FLIR.csv': 0, 'TRV.csv': 1, 'FE.csv': 0, 'DHR.csv': 1, 'MSI.csv': -1, 'VIAB.csv': -1, 'MCHP.csv': 1, 'RE.csv': 1, 'DG.csv': 1, 'VRSN.csv': 1, 'DIS.csv': 1, 'ADSK.csv': 1, 'PFE.csv': 1, 'PM.csv': 1, 'VZ.csv': 0, 'SYK.csv': 1, 'TDG.csv': 1, '_oil.csv': -1, 'HUM.csv': 0, 'COG.csv': -1, 'BA.csv': 1, 'SCHW.csv': 1, 'XRAY.csv': 1, 'FIS.csv': 1, 'QCOM.csv': 1, 'D.csv': 0, 'SO.csv': 0, 'BRK.B.csv': 1, 'UNM.csv': 1, 'RCL.csv': 1, 'KSS.csv': 1, 'DISCK.csv': 0, 'AVB.csv': 1, 'LNC.csv': 1, 'OXY.csv': -1, 'ORCL.csv': 0, 'CTXS.csv': 1, 'CME.csv': 1, 'HCP.csv': 1, 'PKI.csv': 1, 'TAP.csv': 0, 'PG.csv': 1, 'M.csv': 1, 'OKE.csv': 1, 'ANTM.csv': 1, 'LNT.csv': 0, 'AKAM.csv': 1, 'NKE.csv': 1, 'FL.csv': 0, 'MAR.csv': 1, 'MTB.csv': 1, 'BXP.csv': 1, 'CXO.csv': -1, 'TSCO.csv': 0, 'ORLY.csv': 0, 'AES.csv': 0, 'HAS.csv': 1, 'MGM.csv': 1, 'MAA.csv': 1, 'SBUX.csv': 1, 'COO.csv': 1, 'DPS.csv': 1, 'LEG.csv': 1, 'ANSS.csv': 1, 'CHD.csv': 0, 'PPL.csv': 0, 'ALL.csv': 1, 'FISV.csv': 1, 'WHR.csv': 1, 'AAP.csv': 1, 'PPG.csv': 0, 'GRMN.csv': 0, 'BSX.csv': 1, 'GM.csv': 1, 'TROW.csv': 1, 'LUK.csv': 1, 'GPN.csv': 1, 'AMZN.csv': -1, 'NSC.csv': 1, 'EXPE.csv': 1, 'LOW.csv': 1, 'HAL.csv': -1, 'UAL.csv': 1, 'NFLX.csv': 1, 'EXR.csv': 1, 'WMB.csv': 0, 'TMK.csv': 1, 'ZION.csv': 1, 'KLAC.csv': 1, 'ETR.csv': 0, 'ADM.csv': 1, 'CMS.csv': 0, 'ROP.csv': 1, 'SJM.csv': 1, 'PTR.csv': 0, 'KR.csv': 0, 'AIG.csv': 0, 'DFS.csv': 1, 'TXT.csv': 1, 'MCD.csv': 1, 'LUV.csv': 0, 'JBHT.csv': 1, 'NI.csv': 0, 'AOS.csv': 1, 'COF.csv': 1, 'GD.csv': 1, 'ES.csv': 0, 'EL.csv': 1, 'MPC.csv': 0, 'VFC.csv': 0, 'DUK.csv': 0, 'TSS.csv': 1, 'EXC.csv': 1, 'PSA.csv': 1, 'FOXA.csv': 1, 'SIG.csv': 1, 'BWA.csv': 1, 'ABT.csv': 1, 'IDXX.csv': 1, 'MAC.csv': 1, 'HES.csv': -1, 'EIX.csv': 0, 'JPM.csv': 1, 'AEE.csv': 0, 'CMI.csv': 1, 'HRL.csv': 0, 'AXP.csv': 1, 'ISRG.csv': 1, 'DGX.csv': 1, 'LLY.csv': 1, 'VTR.csv': 1, 'BP.csv': 0, 'DISCA.csv': 1, 'XRX.csv': 1, 'HRS.csv': 1, 'PNC.csv': 1, 'LB.csv': 1, 'PAYX.csv': 1, 'GLW.csv': 1, 'FRT.csv': 0, 'EQT.csv': -1, 'AMGN.csv': 0, 'IPG.csv': 0, 'APA.csv': 0, 'IP.csv': 1, 'KMX.csv': 1, 'C.csv': 1, 'NRG.csv': -1, 'RSG.csv': 1, 'AME.csv': 1, 'EQR.csv': 1, 'WMT.csv': 1, 'ESRX.csv': 1, 'HBI.csv': 1, 'ALXN.csv': 1, 'ENB.csv': 0, 'GPC.csv': 0, 'LEN.csv': 1, 'PCLN.csv': 0, 'IBM.csv': 1, 'PCG.csv': 1, 'MLM.csv': 1, 'UNH.csv': 0, 'WYN.csv': 1, 'DRE.csv': 1, 'DISH.csv': 1, 'BF.B.csv': 0, 'BDX.csv': 1, 'WM.csv': 0, 'DTE.csv': 0, 'EMN.csv': 0, 'SYY.csv': 0, 'TEL.csv': 1, 'AIZ.csv': -1, 'KO.csv': 1, 'ETFC.csv': 1, 'LKQ.csv': 0, 'CMCSA.csv': 0, 'LRCX.csv': 1, 'FMC.csv': 0, 'BMY.csv': 1, 'MAT.csv': 0, 'KMB.csv': 1, 'DVN.csv': 0, 'NUE.csv': 1, 'FLR.csv': 1, 'TSN.csv': 0, 'DOV.csv': 1, 'SYMC.csv': 1, 'TJX.csv': 1, 'FOX.csv': 1, 'BEN.csv': 1, 'URI.csv': 0, 'NOC.csv': 1, 'GWW.csv': 1, 'ROK.csv': 1, 'RTN.csv': 1, 'CINF.csv': 1, 'GE.csv': 1, 'ITW.csv': 1, 'XEC.csv': -1, 'GS.csv': 1, 'SRCL.csv': 0, 'WDC.csv': 0, 'NEE.csv': 0, 'KMI.csv': -1, 'CHK.csv': 0, 'JWN.csv': 1, 'UAA.csv': 1, 'MRK.csv': 1, 'IFF.csv': 1, 'AZO.csv': 0, 'ILMN.csv': -1, 'PLD.csv': 1, 'MCO.csv': 1, 'APD.csv': 1, 'FDX.csv': 1, 'PDCO.csv': 1, 'HON.csv': 1, 'RJF.csv': 1, 'MS.csv': 1, 'CF.csv': -1, 'NFX.csv': 1, 'CNC.csv': 0, 'SPGI.csv': 1, 'LH.csv': 1, 'HOLX.csv': 1, 'CELG.csv': 1, 'BIIB.csv': 0, 'K.csv': 0, 'RHT.csv': 0, 'MAS.csv': 1, 'ALK.csv': 1, 'XOM.csv': 1, 'HIG.csv': 1, 'OMC.csv': 1, 'PEP.csv': 1, 'IT.csv': 1, 'PCAR.csv': 1, 'EMR.csv': 1, 'AVY.csv': 1, 'BCR.csv': 1, 'CLX.csv': 1, 'HCA.csv': 0, 'CPB.csv': 0, 'AMP.csv': 1, 'AWK.csv': 0, 'NEM.csv': -1, 'ALGN.csv': 1, 'INCY.csv': 1, 'INTU.csv': 1, 'ABC.csv': 1, 'CVX.csv': 0, 'T.csv': 1, 'BBT.csv': 1, 'HBAN.csv': 1, 'DRI.csv': 1, 'COL.csv': 0, 'YUM.csv': 1, 'PRU.csv': 1, 'REG.csv': 1, 'CTSH.csv': 1, 'CRM.csv': 1, 'HSIC.csv': 1, 'WYNN.csv': 1, 'CAG.csv': 1, 'PNW.csv': 0, 'PWR.csv': 1, 'FAST.csv': 0, 'GOOGL.csv': 1, 'PGR.csv': 1, 'FFIV.csv': 1, 'APH.csv': 1, 'TXN.csv': 0, 'ACN.csv': 1, 'VRSK.csv': 1, 'ROST.csv': 1, 'PH.csv': 1, 'CAH.csv': 0, 'DHI.csv': 1, 'UDR.csv': 1, 'GGP.csv': 0, 'PVH.csv': 1, 'MO.csv': -1, 'SPG.csv': 1, 'MHK.csv': 1, 'PBCT.csv': 1, 'HST.csv': 1, 'NOV.csv': -1, 'CB.csv': 1, 'ADBE.csv': 1, 'AIV.csv': 1, 'CHRW.csv': 0, 'EXPD.csv': 1, 'TMO.csv': 1, 'SWKS.csv': 1, 'AMD.csv': 1, 'DE.csv': 1, 'MU.csv': 1, 'BLL.csv': 1, 'CMA.csv': 1, 'ECL.csv': 0, 'WY.csv': 1, 'FCX.csv': -1, 'MCK.csv': 1, 'PFG.csv': 1, 'JEC.csv': 1, 'FITB.csv': 1, 'SHW.csv': 1, 'SNA.csv': 1, 'PKG.csv': -1, 'BAX.csv': 1, 'MOS.csv': 0, 'EW.csv': 1, 'CL.csv': 1, 'SEE.csv': 1, 'LLL.csv': 1, 'SLG.csv': 1, 'APC.csv': 0, 'AMG.csv': 1, 'REGN.csv': 1, 'ARNC.csv': 1, 'USB.csv': 1, 'MTD.csv': 1, 'DLR.csv': 0, 'COST.csv': 1, 'DLTR.csv': 1, 'HSY.csv': 1, 'TWX.csv': -1, 'WAT.csv': 1, 'BK.csv': 1, 'XLNX.csv': 1, 'AET.csv': 0, 'KIM.csv': 1, 'NTAP.csv': 1, 'NDAQ.csv': 1, 'BAC.csv': 1, 'HPQ.csv': 0, 'UHS.csv': 1, 'A.csv': 1, 'GOOG.csv': 1, 'CSCO.csv': 1, 'STX.csv': -1, 'CVS.csv': 0, 'HRB.csv': 1, 'RF.csv': 1, 'SPLS.csv': 1, 'CMG.csv': 1, 'BLK.csv': 1, 'LYB.csv': 0, 'PX.csv': 0, 'MRO.csv': 0, 'WFC.csv': 1, 'STI.csv': 1, 'RHI.csv': 1, 'SWK.csv': 1, 'HD.csv': 1, 'CAT.csv': 1, 'XEL.csv': 0, 'NVDA.csv': -1, 'ARE.csv': 1, 'PEG.csv': -1, 'CBS.csv': 1, 'MKC.csv': 1, 'F.csv': 1, 'BBY.csv': 1, 'AEP.csv': 0, 'MMM.csv': 1, 'ED.csv': 0, 'UPS.csv': 1, 'RRC.csv': -1, 'COP.csv': 0, 'V.csv': 0, 'L.csv': 1, 'KSU.csv': 1, 'AAPL.csv': 1, 'UTX.csv': 1, 'INTC.csv': 1, 'O.csv': 1, 'DAL.csv': 1, 'RMD.csv': 1, 'TIF.csv': 0, 'ESS.csv': 1, 'PXD.csv': -1, 'RL.csv': 1, 'VRTX.csv': 1, 'SRE.csv': 1, 'KEY.csv': 1, 'MET.csv': 0, 'HP.csv': -1, 'CTL.csv': 1, 'IR.csv': 1, 'STT.csv': 1, 'GPS.csv': 1, 'ANDV.csv': 1, 'DVA.csv': 0, 'ZBH.csv': 1, 'WLTW.csv': 1, 'VNO.csv': 1, 'HOG.csv': 1, 'FLS.csv': 1, 'SU.csv': -1, 'AFL.csv': 1, 'MMC.csv': 1, 'CI.csv': 1, 'SCG.csv': 0, 'WEC.csv': 0, 'CNP.csv': -1, 'MON.csv': 0, 'CA.csv': 1, 'STZ.csv': 1, 'EBAY.csv': 1, 'VAR.csv': 1, 'ADS.csv': 1}

error = 0
total = 0

true_keys = true.keys()

for key in guesses.keys():
	if(key in true_keys):
		error += abs(true[key]-sigmasoid(guesses[key]))
		total += 1

print float(error)/total




	    	
