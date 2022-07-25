
# Flask code to read ai model and response prediction (0 to 1)

# from crypt import methods
#import json
from flask import Flask, jsonify, send_from_directory, request

# import tensorflow as tf
# import numpy as np
# import pandas as pd

app = Flask(__name__)
@app.route('/hello',methods = ['GET'])
def sayHello():
    return "hello"

# #loading ai model globally 
# model = tf.keras.models.load_model('fraud_detection_01.h5')
# #loading mock json file
# with open('mock/user_mock.json','r') as user_file:
#     user_json = json.loads(user_file.read())

# with open('mock/atms.json','r') as user_file:
#     atm_json = json.loads(user_file.read())

# with open('mock/payee.json','r') as user_file:
#     payee_json = json.loads(user_file.read())

# with open('mock/merchants.json','r') as user_file:
#     merchant_json = json.loads(user_file.read())

# #define min max for model for prediction

#  # build min and max value
#     X_min = pd.DataFrame(
#         {
#             'step': [1.0],
#             'amount':[0.0],
#             'nameOrig': [1338.0],
#             'oldbalanceOrg': [0.0],
#             'newbalanceOrig': [0.0],
#             'nameDest':             [2.0],
#             'oldbalanceDest':       [0.0],
#             'newbalanceDest':       [0.0],
#             'isFlaggedFraud':       [0.0],
#             'type_CASH_IN':         [0.0],
#             'type_CASH_OUT':        [0.0],
#             'type_DEBIT':           [0.0],
#             'type_PAYMENT':         [0.0],
#             'type_TRANSFER':        [0.0]
#         }
#     )

#     X_max = pd.DataFrame(
#             {
#                 'step' :             [743.00],
#                 'amount' :           [9244552.00],
#                 'nameOrig' :         [2147484000.00],
#                 'oldbalanceOrg':     [59585040.00],
#                 'newbalanceOrig' :   [49585040.00],
#                 'nameDest' :         [2147483000.00],
#                 'oldbalanceDest':    [356015900.00],
#                 'newbalanceDest' :   [356179300.00],
#                 'isFlaggedFraud' :   [1.0],
#                 'type_CASH_IN' :     [1.0],
#                 'type_CASH_OUT':     [1.0],
#                 'type_DEBIT'  :      [1.0],
#                 'type_PAYMENT':      [1.0],
#                 'type_TRANSFER':     [1.0]
#             }
#     )



# @app.route('/login/<userid>',methods = ['GET'])
# def login(userid):
    
#     print(user_json[0]['user_id'])
#     for user in user_json:
#         if user['user_id'] == userid:

#             return jsonify(userName = user['username'],
#                     status = "success",
#                     accounts = user['accounts']
            
#             )
#     return jsonify(
#         status = "failure"
#     )
# @app.route('/predict',methods = ['POST'])
# def predictFraud():

#     params = request.json
#     #getting request data
#     request_data = {
#         'step' : [params["step"]],
#         'nameOrig' : [params["nameOrig"]],
#         'amount' : [params["amount"]],
#         'nameDest' : [params["nameDest"]],
#         'oldbalanceOrg' : [params["oldbalanceOrg"]],
#         'newbalanceOrig' : [params["newbalanceOrig"]],
#         'oldbalanceDest' : [params["oldbalanceDest"]],
#         'newbalanceDest' : [params["newbalanceDest"]],
#         'isFlaggedFraud' : [params["isFlaggedFraud"]],
#         'type' : [params["type"]],
#     }

#     #convert input to data frame
#     request_df = pd.DataFrame(request_data)

#     #preprocess data removing first character of origin and destination code
#     request_df['nameOrig'] = request_df['nameOrig'].str[1:]
#     request_df['nameDest'] = request_df['nameDest'].str[1:]
#     request_df = pd.get_dummies(request_df,columns = ['type'])

#     request_df = request_df.astype(np.float32)
#     X_maxx = X_max.astype(np.float32)
#     X_minn = X_min.astype(np.float32)

#     print(request_df)  
#     #convert to imput between 0 and 1  
#     X_data = ( request_df - X_minn)/(X_maxx-X_minn)
#     X_data =  X_data.fillna(0.0)
    
#     print(X_data)
#     print("Calculating prediction ....")
#     #model predict 
#     pred = model.predict(
#          X_data
#         )
    
#     print(pred)

#     #return predict
#     return jsonify(
#         prediction = str(format(pred[0][0],'f'))
#     )
   

# @app.route('/atms',methods = ['GET'])
# def getAtms():
    
#     return jsonify(
#       atms =  atm_json
#     )
    
# @app.route('/merchants',methods = ['GET'])
# def getMerchants():
#     return jsonify(
#     merchants = merchant_json
#     )

# @app.route('/payees',methods = ['GET'])  
# def getPayee():
#     return jsonify(
#         payee = payee_json
#     )

# @app.route('/image/<path:filename>',methods = ['GET'])
# def getImage(filename):
#     print(filename)
#     return send_from_directory(app.static_folder,filename,as_attachment=False)

# @app.route('/txntype',methods = ['GET'])  
# def getTxnType():
#     return jsonify(
#         type = [{'CASH_OUT' : 'Cash out'},{'TRANSFER' : 'Fund Transfer'},{'PAYMENT' : 'Payment'},{'CASH_IN' : 'Cash Received'},{'DEBIT' : 'Account debit'}]
#     )

if __name__ == '__main__':
    app.run(debug=True)

