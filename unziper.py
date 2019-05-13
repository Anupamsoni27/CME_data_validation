# import os,zipfile
# dataset_name = "CME_NYMEX_D0"
# inputfile_name_pattern = "2000_XNYM_CDF.csv"
#
# for  root, dirs, files  in os.walk(r"C:\Users\anupam.soni\Downloads\aa"):
#     for file in files:
#         if file.endswith(".zip"):
#             print(file)
#             archive = zipfile.ZipFile(root+"\\"+file)
#             for file_1 in archive.namelist():
#                 # print( file_1.split("_")[1] , str(inputfile_name_pattern.split("_")[1]) )
#                 if file_1.split("_")[-1].split(".")[0] == dataset_name.split("_")[-1] and \
#                         file_1.split("_")[1] == str(inputfile_name_pattern.split("_")[1]) :
#                     print(file_1)
import json,os

global exchange_code, category_code, contrct_code, contrct_month, \
    model_profile, temp_date, value

gdm_json = open("gdm_data/dict.json")
gdm_json = json.load(gdm_json)
path = ""


def checkinput(exchange_code, category_code, contrct_year, contrct_month, model_profile, temp_date,
               value,total_models,validated_models ):
    global row
    row_o = "Validated " + validated_models + "models out of " + total_models
    row = ""
    id = str(temp_date.replace("-", "")) + "." + contrct_year + "." + contrct_month
    for temp_id in input_json:
        # print(temp_id)
        if temp_id.endswith(id):
            # print(temp_id)
            if input_json[temp_id]["Product Code"] == category_code:
                if model_profile == "SETTLE":
                    if input_json[temp_id]["Settlement"] != value:
                        print(input_json[temp_id]["Settlement"], value)

                        row = str("issue found for " + str(model) + " Date : " + temp_date)
                        print(row)
                        break
                        # temp_obj  =  front_end.Ui_Form()
                        # # temp_obj.refresh_text_box(row)
                        # print("***********")

                    # if input_json[temp_id][elements]


for root, dir, files2 in os.walk(path + "input_json/"):
    for file2 in files2:
        input_json = open(path + "input_json/" + file2)
        input_json = json.load(input_json)
        total_models = len(gdm_json)
        validated_models = 0
        for model in gdm_json:
            validated_models = validated_models + 1
            print(model)

            global exchange_code, category_code, contrct_year, contrct_month, \
                model_profile, temp_date, value

            if model != "Model Code":
                exchange_code = model.split(".")[1]
                category_code = model.split(".")[5]
                contrct_year = model.split(".")[6].split("M")[0]
                contrct_month = model.split(".")[6].split("M")[1][:2]
                model_profile = model.split("/")[-2]

                # for key in gdm_json[model]:
                #     print(key, gdm_json[model][key])
                for date in gdm_json[model]:
                    # print(date, gdm_json[model][date])
                    temp_date = date
                    value = gdm_json[model][date]
                    if not temp_date.startswith("description"):
                        # print("Checking: ",exchange_code, category_code, contrct_year, contrct_month, model_profile, temp_date, value)
                        checkinput(exchange_code, category_code, contrct_year, contrct_month, model_profile, temp_date,
                                   value,total_models,validated_models)
                        # print(exchange_code, category_code, contrct_year, contrct_month, model_profile, temp_date,
                        #            value)
                        # print("%%%%%")
                        if len(row) > 0:

                            print(row)