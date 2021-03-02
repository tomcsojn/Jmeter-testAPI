# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:39:26 2021

@author: Tamas
"""

from flask import Flask,request,jsonify,abort
# import json
# %%init
app = Flask(__name__)



# %%endpoint1

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
# %%endpoint2




#%%Main
if __name__ == '__main__':    

    app.run(host='127.0.0.1',port=5000)