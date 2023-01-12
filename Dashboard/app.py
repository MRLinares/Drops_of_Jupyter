# import libraris
import pandas as pd

import numpy as np
from flask import Flask, render_template, request
import pickle

## col names for df
col_names = ['Weight_Lbs',
            'Age', 
            'Poverty_Ratio',
            'Prediabetes_no', 
            'Prediabetes_yes', 
            'Categorical_BMI_Healthy_Weight',
            'Categorical_BMI_Obese', 
            'Categorical_BMI_Overweight',
            'Categorical_BMI_Underweight',  
            'Gender_Female', 
            'Gender_Male',
            'Education_12th_Grade_no_diploma',
            'Education_Associates_Academic_Program',
            'Education_Associates_Occupational_Technical_Vocational',
            'Education_Bachelor', 
            'Education_GED_Equivalent',
            'Education_Grade_1-11', 
            'Education_Greater_Than_Master',
            'Education_High_School_Graduate', 
            'Education_Masters',
            'Education_Some_College_no_degree', 
            'Race_AIAN_AND_other',
            'Race_AIAN_Only',
            'Race_African_American_Only', 
            'Race_Asian_Only',
            'Race_Other',
            'Race_White_Only']


# initialzie the flask app
app = Flask(__name__)

# load ml model
std_scaler = pickle.load(open('scaler.pkl','rb'))
model = pickle.load(open('model.pkl', 'rb'))

# define the app route for the default page of the web-app
@app.route('/')
def home():
    return render_template('index.html')

# to use the predict button in our web-app
@app.route('/predict', methods=['POST'])
def predict():

    X = np.zeros( len(col_names) )
    print(len(col_names))
    print("X",X)
    df_XX = pd.DataFrame(data=[dict(zip(col_names, X) ) ] )

    # for rending result on html GUI

    feat_prediabetic = f"Prediabetes_{request.form['prediabetes']}"
    print( "Feat_prediabetic:", feat_prediabetic)
    df_XX[ feat_prediabetic ] = 1.0

    feat_weightlbs = int( request.form['weightlbs'] )
    print( "Feat weightlbs:", feat_weightlbs)
    df_XX['Weight_Lbs']=feat_weightlbs

    feat_height = int( request.form['height'] )
    print( "Feat height:", feat_height )

    bmi = 703 * ( feat_weightlbs / (feat_height * feat_height) )
    print( "Feat bmi:", bmi )

    if bmi <= 18.5:
        df_XX['Categorical_BMI_Underweight'] = 1.0
    elif bmi > 18.5 and bmi < 25:
        df_XX['Categorical_BMI_Healthy_Weight'] = 1.0
    elif bmi >= 25 and bmi < 30:
        df_XX['Categorical_BMI_Overweight'] = 1.0
    else:
        df_XX['Categorical_BMI_Obese'] = 1.0
    
    feat_age = int( request.form[ 'age'])
    print( "Feat age:", feat_age )
    df_XX['Age'] = feat_age

    feat_gender = f"Gender_{request.form['gender']}"
    print("Feat Gen:",feat_gender)
    df_XX[ feat_gender ] = 1.0

    feat_education = f"Education_{request.form['education']}"
    print("Feat Edu:",feat_education)
    df_XX[ feat_education ] = 1.0

    feat_race = f"Race_{request.form['race']}"
    print("Feat Race:", feat_race)
    df_XX[ feat_race ] = 1.0

    feat_hhincome = float( request.form['income'] )
    print( "Feat_hhincome:", feat_hhincome)

    feat_hhsize = int( request.form['size'] )
    print( "Feat_hhsize:", feat_hhsize)

    ratio = feat_hhincome/(8340+(feat_hhsize*4540))
    print( "Feat_ratio:", ratio)
    df_XX[ 'Poverty_Ratio' ] = ratio
    
    print( df_XX )
    #Loading model to compare the results
    scaled_input = std_scaler.transform(df_XX)
    print(scaled_input)
    #int_features = [float(x) for x in df_XX.iloc[0]]
    #print(int_features)
    #final_features = [np.array(int_features)]
    prediction = model.predict_proba( scaled_input )
    print("prediction",prediction)
    
    output = np.round(prediction[0][1], 2)

    print( 'You are likely: {}'.format(output) )

    if output > (.65):
        page = "sad.html"
    else:
        page = "happy.html"
    return render_template(page, prediction_text='Probability: {}'.format(output))

# start the flask server
if __name__ == '__main__':
    app.run(debug=True)