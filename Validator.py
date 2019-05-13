import json
import front_end
class Validator():
    def __init__(self):
        pass




    def main(self):
        global exchange_code, category_code, contrct_code, contrct_month, \
            model_profile,temp_date, value

        gdm_json = open("gdm_data/dict.json")
        gdm_json = json.load(gdm_json)

        input_json = open("input_json/2015_XNYM_D0.json")
        input_json = json.load(input_json)

        for model in gdm_json:
            print(model)
            def checkinput(exchange_code, category_code, contrct_year, contrct_month, model_profile, temp_date, value):

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
                                    temp_obj  =  front_end.Ui_Form()
                                    # temp_obj.refresh_text_box(row)
                                    print("***********")

                                # if input_json[temp_id][elements]

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
                    # print("Checking: ",exchange_code, category_code, contrct_year, contrct_month, model_profile, temp_date, value)
                    checkinput(exchange_code, category_code, contrct_year, contrct_month, model_profile, temp_date, value)


