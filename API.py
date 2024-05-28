from flask import Flask
from flask import request
import pandas as pd
import pickle
import os
from random import randint

def LoadFile(Path):
    if os.path.isfile(Path):
        with open(Path, 'rb') as fp:
            return pickle.load(fp)
    else:
        return -1


regressor = LoadFile("model.pkl")

app = Flask(__name__)


@app.route("/api/devices/<Flag>", methods=["GET",'POST'])
def devices(Flag):
    if request.method == "GET":
        if Flag.isnumeric():
            df = pd.read_csv("test.csv")

            deviceDF = df.loc[df["id"] == int(Flag)]
            jsonData = deviceDF.to_json(orient="records")

            return jsonData
        else:
            return {"result": "Unknown API"}
    else:
        if Flag.lower() == "add":
            d = request.data
            if len(d) == 0:
                return {"result":"No data has been provided to add it"}
            Data = request.json
            df = pd.read_csv("test.csv")
            IDs = df["id"].tolist()
            MaxId = max(IDs)
            df.loc[len(df.index)] = [MaxId + 1, Data["battery_power"], Data["blue"], Data["clock_speed"], Data["dual_sim"],
                                     Data["fc"], Data["four_g"],
                                     Data["int_memory"], Data["m_dep"], Data["mobile_wt"], Data["n_cores"], Data["pc"],
                                     Data["px_height"],
                                     Data["px_width"], Data["ram"], Data["sc_h"], Data["sc_w"], Data["talk_time"],
                                     Data["three_g"],
                                     Data["touch_screen"], Data["wifi"]]

            df.to_csv("test.csv", index=False)

            return {"result": "New Device Added Successfully"}

        elif Flag.lower() == "get":
            df = pd.read_csv("test.csv")
            jsonData = df.to_json(orient="records")

            return jsonData
        else:
            return {"result": "Unknown API"}

@app.route("/api/predict/<id>", methods=['POST'])
def predict(id):
    classes = {0:"Low Cost",
               1:"Meduim Cost",
               2: "High Cost",
               3: "Very high cost"}

    df = pd.read_csv("test.csv")

    if id.isnumeric():
        df_ = df.loc[df["id"] == int(id)]
        if len(df.index) == 0:
            return {"result": "No Such ID is exist"}

        df_ = df_.drop(columns="id",axis=1)



        result = regressor.predict(df_)[0]
        if result == 0:
            res = {"result":classes[0]}
        elif result == 1:
            res = {"result": classes[1]}
        elif result == 2:
            res = {"result": classes[2]}
        elif result == 3:
            res = {"result": classes[3]}
        return res

    elif id.lower() == "ten":
        resultDict = {}
        listofIds = df["id"].tolist()
        for i in range(10):
            ID = randint(0,len(listofIds))
            df_ = df.loc[df["id"] == int(listofIds[ID])]
            if len(df.index) == 0:
                return {"result": "No Such ID is exist"}

            df_ = df_.drop(columns="id", axis=1)

            result = regressor.predict(df_)[0]
            resultDict[listofIds[ID]] = classes[result]


        return {"result":resultDict}
    else:
        return {"result": "Unknown API"}



if __name__ == "__main__":
    app.run('0.0.0.0',port = 7000)
