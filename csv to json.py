import csv
import json
dict = {}
file  = open(r"C:\Users\anupam.soni\PycharmProjects\CME_Validarion\inputfiles\2015_XNYM_D0.csv")
reader = csv.reader(file)
model_list = []
file_prefix  = "2015_XNYM_D0"

for row in reader:
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])] = {}
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Exchange Code"] = row[1]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Asset Class"] = row[2]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Product Code"] = row[3]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Clearing Code"] = row[4]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Product Description"] = row[5]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Product Type"] = row[6]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Underlying Product Code"] = row[7]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Put/Call"] = row[8]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Strike Price"] = row[9]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Contract Year"] = row[10]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Contract Month"] = row[11]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Contract Day"] = row[12]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Settlement"] = row[13]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Settlement Cabinet Indicator"] = row[14]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Open Interest"] = row[15]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Total Volume"] = row[16]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex Volume"] = row[17]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Volume"] = row[18]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["PNT Volume"] = row[19]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Block Volume"] = row[20]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["EFP Volume"] = row[21]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["EOO Volume"] = row[22]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["EFR Volume"] = row[23]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["EFS Volume"] = row[24]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["EFB Volume"] = row[25]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["EFM Volume"] = row[26]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["SUB Volume"] = row[27]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["OPNT Volume"] = row[28]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["TAS Volume"] = row[29]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["TAS Block Volume"] = row[30]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["TAM Singapore Volume"] = row[31]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["TAM Singapore Block Volume"] = row[32]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["TAM London Volume"] = row[33]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["TAM London Block Volume"] = row[34]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex Open Price"] = row[35]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex Open Price Bid/Ask Indicator"] = row[36]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex Open Price Cabinet Indicator"] = row[37]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex High Price"] = row[38]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex High Price Bid/Ask Indicator"] = row[39]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex High Price Cabinet Indicator"] = row[40]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex Low Price"] = row[41]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex Low Price Bid/Ask Indicator"] = row[42]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex Low Price Cabinet Indicator"] = row[43]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex Close Price"] = row[44]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex Close Price Bid/Ask Indicator"] = row[45]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Globex Close Price Cabinet Indicator"] = row[46]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Open Price"] = row[47]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Open Price Bid/Ask Indicator"] = row[48]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Open Price Cabinet Indicator"] = row[49]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Open Second Price"] = row[50]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Open Second Price Bid/Ask Indicator"] = row[51]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor High Price"] = row[52]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor High Price Bid/Ask Indicator"] = row[53]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor High Price Cabinet Indicator"] = row[54]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Low Price"] = row[55]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Low Price Bid/Ask Indicator"] =  row[56]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Low Price Cabinet Indicator"] =  row[57]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Close Price"] = row[58]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Close Price Bid/Ask Indicator"] = row[59]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Close Price Cabinet Indicator"] = row[60]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Close Second Price"] = row[61]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Close Second Price Bid/Ask Indicator"] = row[62]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Post-Close Price"] = row[63]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Post-Close Price Bid/Ask Indicator"] = row[64]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Post-Close Second Price"] = row[65]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Floor Post-Close Second Price Bid/Ask Indicator"] = row[66]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Delta"] = row[67]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Implied Volatility"] = row[68]
    dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])]["Last Trade Date"] = row[69]


# dict[model] = {row[0],row[1],row[2],row[3]}
print(dict)
json = json.dumps(dict, indent=4)
f = open("input_dict.json","w")
f.write(json)
f.close()