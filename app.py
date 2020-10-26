from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('XGBoost_model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('html.html')

@app.route("/predict", methods=['POST'])
def predict():
    Property_Area_Semiurban = 0
    if request.method == 'POST':
        Credit_History = request.form['Credit_History']
        if(Credit_History == 'Yes'):
            Credit_History = 1
        else:
            Credit_History = 0
        Gender_Male = request.form.get("Gender_Male", False)
        if(Gender_Male == 'Male'):
            Gender_Male = 1
        else:
            Gender_Male = 0
        Married_Yes = request.form.get('Married_Yes', False)
        if(Married_Yes == 'Yes'):
            Married_Yes = 1
        else:
            Married_Yes = 0
        Property_Area_Urban = request.form.get('Property_Area_Urban', False)
        if(Property_Area_Urban == 'Urban'):
            Property_Area_Urban = 1
            Property_Area_Semiurban = 0
        else:
            Property_Area_Urban = 0
            Property_Area_Semiurban = 1
        Total_Income = float(request.form['Total_Income'])
        EMI = float(request.form['EMI'])
        prediction=model.predict([[Credit_History, Gender_Male, Married_Yes,Property_Area_Semiurban, Property_Area_Urban, Total_Income,EMI]])
        if (prediction == 0):
            return render_template('html.html',prediction_text="Opps !!...Sorry you cannot get the loan")
            
        else:
            return render_template('html.html', prediction_text="Hurrah !!...you can get the loan")
    
  

if __name__=="__main__":
    app.run(debug=True)
