import csv,os
from builtins import print
global data
from pandas import DataFrame
from PyQt5 import QtCore, QtWidgets
import pymssql
import time,zipfile
import datacall
from PyQt5.QtCore import Qt, QThread, pyqtSignal
#path = ""
path = r"C://python_tool//CME_Validation//"
#input_path = r"C://Users//anupam.soni//Downloads//aa//"
input_path = r"C://python_tool//CME_INPUT_FILES//"
class Ui_Form(object):

    def __init__(self):
        super().__init__()

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(1071, 600)	
        Form.setFixedSize(1071, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1051, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(input_path)
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        # self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        # self.lineEdit_2.setObjectName("lineEdit_2")
        # self.lineEdit_2.setText("r")
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)

        self.comboBox_2.setObjectName("comboBox")
        self.comboBox_2.addItem("Select Dataset")
        self.comboBox_2.setEnabled(False)
        self.gridLayout.addWidget(self.comboBox_2,  1, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_3.addWidget(self.checkBox_5)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setEnabled(False)
        self.horizontalLayout_3.addWidget(self.dateEdit)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_3.addWidget(self.checkBox_6)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.dateEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.setEnabled(False)

        self.horizontalLayout.addWidget(self.checkBox_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.setEnabled(False)
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setEnabled(False)
        self.horizontalLayout.addWidget(self.checkBox)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 180, 1051, 350))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(2, 1, 1, 1)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.lineEdit_2.setText("Output path : "+str(os.path.expanduser("~/Desktop")))
        self.lineEdit_2.setEnabled(False)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.gridLayout_2.addWidget(self.pushButton_3, 3, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        # self.pushButton_3.setEnabled(False)


        self.pushButton_4.setObjectName("pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 3, 2,1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)
        self.plainTextEdit = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CME Validation"))
        self.label.setText(_translate("Form", "Input File Path :"))
        self.label_5.setText(_translate("Form", "Start Range : "))
        self.label_6.setText(_translate("Form", "Input File name(Sample) : "))
        self.label_4.setText(_translate("Form", "Hub Server :"))
        self.label_3.setText(_translate("Form", "Dataset Name : "))
        self.label_2.setText(_translate("Form", "Check Profile : "))
        self.comboBox.setItemText(0, _translate("Form", "Select Server"))
        self.comboBox.setItemText(1, _translate("Form", "DHUB-1"))
        self.comboBox.setItemText(2, _translate("Form", "DHUB-2"))
        # self.comboBox.setItemText(3, _translate("Form", "UAT Tesr Server"))
        self.checkBox_5.setText(_translate("Form", "Default"))
        self.label_7.setText(_translate("Form", "End Range : "))
        self.checkBox_6.setText(_translate("Form", "Default"))
        self.checkBox_2.setText(_translate("Form", "Settle"))
        self.checkBox_4.setText(_translate("Form", "VOL"))
        self.checkBox_3.setText(_translate("Form", "OI"))
        self.checkBox.setText(_translate("Form", "Check all"))
        # self.pushButton_3.setText(_translate("Form", "Export result"))
        self.pushButton_4.setText(_translate("Form", "Close"))
        self.pushButton.setText(_translate("Form", "Run"))
        self.checkBox_5.setChecked(True)
        self.checkBox_6.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox.clicked.connect(self.check_all_profiles)
        self.checkBox_5.clicked.connect(self.set_editdate_state_1)
        self.checkBox_6.clicked.connect(self.set_editdate_state_2)
        self.comboBox.currentTextChanged.connect(self.call)
        # self.pushButton_3.clicked.connect()
        # self.plainTextEdit.append('o')  # append string
        # self.plainTextEdit.append('o')  # append string
        print(str(self.lineEdit.text())+ "  assigned     ")

        # self.pushButton.clicked.connect(self.show_bucket_crated_successfully)

        self.pushButton.clicked.connect(self.startProgressBar)
        self.pushButton_4.clicked.connect(self.close)

    def check_all_profiles(self):
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)
        self.checkBox_4.setChecked(True)

    def set_editdate_state_1(self):
        self.dateEdit.setEnabled(False)

    def set_editdate_state_2(self):
        self.dateEdit_2.setEnabled(False)

    def desabler(self):
        self.lineEdit.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.comboBox_2.setEnabled(False)
        self.checkBox.setEnabled(False)
        self.checkBox_2.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.checkBox_5.setEnabled(False)
        self.checkBox_6.setEnabled(False)
        self.dateEdit.setEnabled(False)
        self.dateEdit_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.dateEdit.setEnabled(False)
        Ui_Form.inputfile_name_pattern = self.lineEdit_5.text()
        Ui_Form.server = self.comboBox.currentText()
        Ui_Form.dataset_name = self.comboBox_2.currentText()
        self.lineEdit_2.setEnabled(False)

    def call(self):


        folder_path = ""
        server = self.comboBox.currentText()
        # dataset_name = input("Enter dataset category name...")
        # eia_data_file_name = input("Enter EIA data file name...")
        # server = input("Enter server name...")
        if server == "DHUB-1":
            server_name = "10.0.0.00"
            user_name = "gdmdhub"
            pswd = "gdmdhub"
            database_name = "GDM"
            api_server = "http://10.0.0.000:80"
        elif server == "DHUB-2":
            server_name = "10.0.0.00"
            user_name = "gdm"
            pswd = "gdm"
            database_name = "GDM"
            api_server = "http://10.0.0.000:80"
        elif server == "UAT Test Server":
            server_name = "10.0.0.00"
            user_name = "GDM_UAT"
            pswd = "GDM_UAT"
            database_name = "GDM_UAT"
            api_server = "http://10.0.0.000:80"





        query_part_1 = """SELECT CODE FROM LIB_TEMPLATE
                                                   WHERE CODE LIKE 'CME%' ORDER BY CODE """
        query_part_2 = ""
        global dhub_1_list
        global dhub_2_list
        global all_list
        dhub_1_list = []
        dhub_2_list = []
        all_list = []
        query = query_part_1

    
        conn = pymssql.connect(server=server_name, user=user_name, password=pswd, database=database_name)
        cursor = conn.cursor()

        # script = "select DISTINCT m.category,m.uri from lib_model m where m.code like'%.[0-9][0-9][0-9][0-9]M%' and m.category like'%REL'"
        script = query
        print(script)
        cursor.execute(script)

        data = cursor.fetchall()
        print(type(data))
        data = list(data)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.clear()
        self.comboBox_2.addItem("Select Dataset")
        for d in data:
            print(list([d]))
            d = str(d).replace("(","")
            d = str(d).replace(")","")
            d = str(d).replace("'","")
            d = str(d).replace(",","")
            self.comboBox_2.addItem(str(d))


    def close(self):
        app.quit()

    def startProgressBar(self):
        self.desabler()
        self.thread = MyThread()
        self.thread.change_value.connect(self.add)


        self.thread.start()



    def add(self,val):
        # print("333333")
        self.plainTextEdit.append(str(val))  # append string
   
class MyThread(QThread,Ui_Form):
    # Create a counter thread
    change_value = pyqtSignal(str)
    def run(self):
        result_list = []
        pack_obj = Pack()
        ui1 = Ui_Form()
        time.sleep(0.3)
        self.change_value.emit("Initializing......")

        self.change_value.emit("Collecting input files.........")
        # print(ui1.comboBox_2.())
        # print(Ui_Form.a)
        pack_obj.take_input(Ui_Form.inputfile_name_pattern, Ui_Form.server,Ui_Form.dataset_name )
        self.change_value.emit("Done !!!")

        self.change_value.emit("Unzipping and fiding files......")
        pack_obj.unzipper()
        self.change_value.emit("Done !!!")
        # ui1.stop_thread()

        self.change_value.emit("Getting data from GDM......")
        dc = datacall.dataCall()
        dc.call(Ui_Form.dataset_name,Ui_Form.server)
        self.change_value.emit("Done !!!")

        self.change_value.emit("Coverting GDM data to json......")
        pack_obj.json_maker()
        self.change_value.emit("Done !!!")

        self.change_value.emit("Coverting input files to json......")
        pack_obj.input_json_maker()
        self.change_value.emit("Done !!!")

        self.change_value.emit("Validation Started......")

        import json
        global exchange_code, category_code, contrct_code, contrct_month, \
            model_profile, temp_date, value

        gdm_json = open(path+"gdm_data/dict.json")
        gdm_json = json.load(gdm_json)
        total_models = len(gdm_json) - 1
        validated_models = 0
        def checkinput(exchange_code, category_code, contrct_year, contrct_month, model_profile, temp_date,
                       value, validated_models,total_models):
            global row, row_o
            row = ""
            row_o = ""
            id = str(temp_date.replace("-", "")) + "." + contrct_year + "." + contrct_month
            for temp_id in input_json:
                # print(temp_id)
                if temp_id.endswith(id):
                    # print(temp_id)
                    if input_json[temp_id]["Product Code"] == category_code:
                        if model_profile == "SETTLE":
                            print(temp_id)
                            if input_json[temp_id]["Settlement"] != value:
                                print(input_json[temp_id]["Settlement"], value)
                                row = str("issue found for " + str(model) + " Date : " + temp_date)
                                result_row = temp_date, Ui_Form.dataset_name, exchange_code, category_code, contrct_year, contrct_month, model_profile, value,input_json[temp_id]["Settlement"]
                                result_list.append(result_row)
                                print(row)
                                break

            row_o = str("Checked " + validated_models + " models out of  " + total_models)

                                # temp_obj  =  front_end.Ui_Form()
                                # # temp_obj.refresh_text_box(row)
                                # print("***********")

                            # if input_json[temp_id][elements]

        for model in gdm_json:
            if model != "Model Code":
                validated_models = validated_models + 1
                print(model)
                for root,dir, files2 in os.walk(path + "input_json/"):
                    for file2 in files2:
                        input_json = open(path + "input_json/"+file2)
                        input_json = json.load(input_json)


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
                                if  not temp_date.startswith("description"):

                                    # print("Checking: ",exchange_code, category_code, contrct_year, contrct_month, model_profile, temp_date, value)
                                    checkinput(exchange_code, category_code, contrct_year, contrct_month, model_profile, temp_date,
                                               value,str(validated_models),str(total_models))
                                    # print(exchange_code, category_code, contrct_year, contrct_month, model_profile, temp_date,
                                    #            value)
                                    # print("%%%%%")
                                    if len(row)> 0:
                                        time.sleep(0.3)
                                        self.change_value.emit(row)
                                        print(row)
                            time.sleep(0.3)
                self.change_value.emit(row_o)
        self.change_value.emit("Validation Done !!!")
        df_00 = DataFrame(result_list,
                          columns=["index date", "Dataset Name", "Exchange code", "Category code", "Contract year",
                                   "Contract month", "Model prifile", "GDM value", "Inputfile Value"])
        # df_00.drop(df_00.columns[0], axis=1)
        from datetime import datetime
        current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
        df_00.to_csv(str(os.path.expanduser("~/Desktop")) + "/"+ str(category_code) +"_"+ str(current_datetime) +".csv", index=False)


class Pack(QThread):
    global zip_file_name, file_extract

    def __init__(self):

        pass

    def take_input(self, val1, val2, val3 ):
        print(val1)
        print(val2)
        print(val3)
        global dataset_name,req_profile, hub_server, range, inputfile_name_pattern
        dataset_name = val3
        # req_profile =
        hub_server = val2
        # range = "aLL"
        inputfile_name_pattern = val1

    def unzipper(self):

        for root, dirs, files in os.walk(input_path):
            for file in files:
                if file.endswith(".zip"):
                    print(file)
                    archive = zipfile.ZipFile(root + "\\" + file)
                    for file_1 in archive.namelist():
                        # print( file_1.split("_")[1] , str(inputfile_name_pattern.split("_")[1]) )
                        if file_1.split("_")[-1].split(".")[0] == dataset_name.split("_")[-1] and \
                                file_1.split("_")[1] == str(inputfile_name_pattern.split("_")[1]):
                            print(file_1)
                            archive.extract(file_1,"inputfiles/")

    def json_maker(self):
        import json
        file = open(path + "model_data.csv")
        reader = csv.reader(file)
        model_list = []
        dict = {}
        for row1 in reader:
            model_list.append(row1[2])
        model_list = list(set(model_list))

        print(model_list)
        for model in model_list:
            dict[model] = {}
            file = open(path + "model_data.csv")
            reader = csv.reader(file)
            print(model)
            for row in reader:
                # print(row)
                # print(row[2], model)
                if row[2] == model and row[2] != "Model Code":
                    dict[model][row[0]] = row[1]
                    dict[model]["description"] = row[3]
                    # dict[model] = {row[0],row[1],row[2],row[3]}

        print(dict)
        json = json.dumps(dict, indent=4)
        f = open(path +"gdm_data/dict.json", "w")
        f.write(json)
        f.close()

    def input_json_maker(self):
        for root,dir, files in os.walk("inputfiles/"):
            for file in files:
                import csv
                import json
                dict = {}
                file1 = open(root+"/"+file)
                reader = csv.reader(file1)
                model_list = []
                file_prefix = file.split(".")[0]
                for row in reader:
                    # dict[file_prefix+"."+str(row[0]) + "." + str(row[10]) + "." + str(row[11])] = {}
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
                f = open(path + "input_json/"+file.split(".")[0]+".json", "w")
                f.write(json)
                f.close()


    def delete_file(self):
        for root, dir, files in os.walk(path + "gdm_data//"):
            for f in files:
                print(path + "gdm_data//"+f)
                os.remove(path + "gdm_data//"+f)
        for root, dir, files in os.walk(path + "input_json//"):
            for f in files:
                print(f)
                os.remove(path + "input_json//"+f)
        for root, dir, files in os.walk(path + "inputfiles//"):
            for f in files:
                print(f)
                os.remove(path + "inputfiles//"+f)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

''