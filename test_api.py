# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:39:26 2021

@author: Tamas
"""

from flask import Flask,request,jsonify,abort,Response
from time import sleep
import pandas as pd
import numpy as np
# import json
# %%init
app = Flask(__name__)



# %%simplejson

@app.route("/getjson")
def returnjson():
    # return jsonify(data=x)
    x = {
	"items":
		{
			"item":
				[
					{
						"id": "0001",
						"type": "donut",
						"name": "Cake",
						"ppu": 0.55,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" },
										{ "id": "1002", "type": "Chocolate" },
										{ "id": "1003", "type": "Blueberry" },
										{ "id": "1004", "type": "Devil's Food" }
									]
							},
						"topping":
							[
								{ "id": "5001", "type": "None" },
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5005", "type": "Sugar" },
								{ "id": "5007", "type": "Powdered Sugar" },
								{ "id": "5006", "type": "Chocolate with Sprinkles" },
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							]
					}

				]
		}
}
    return x
# %%sleepreturn
@app.route("/wait")
def wait():
    sleep(30)
    return "OK"

# %%csv
@app.route("/csv")
def getCsv():
    
    df = pd.DataFrame(np.random.randint(0,10000,size=(100,100)))

    return Response(df.to_csv(),mimetype="text/csv",headers={"Content-disposition":"attachment; filename=myname.csv"})

#%%Main
if __name__ == '__main__':    

    app.run(threaded=False,host='127.0.0.1',port=5000)