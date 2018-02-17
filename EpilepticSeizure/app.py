from flask import Flask,render_template,redirect,url_for,request,session,flash
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import Pipeline
import os
import urllib
from sklearn.model_selection import GridSearchCV, train_test_split, validation_curve, learning_curve
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']= 0
app.secret_key = "Rashmi"
@app.route('/', methods = ['GET','POST'])
def test():

    return render_template("index.html")

@app.route('/form_submit', methods = ['POST'])
def form_submit():
    my_list =[]
    my_list.append(float(request.form['X95']))
    my_list.append(float(request.form['X101']))
    my_list.append(float(request.form['X106']))
    my_list.append(float(request.form['X111']))
    my_list.append(float(request.form['X116']))
    my_list.append(float(request.form['X121']))
    my_list.append(float(request.form['X127']))
    my_list.append(float(request.form['X144']))
    my_list.append(float(request.form['X153']))
    my_list.append(float(request.form['X156']))
    my_list.append(float(request.form['X160']))
    my_list.append(float(request.form['X161']))
    my_list.append(float(request.form['X169']))
    my_list.append(float(request.form['X171']))
    my_list.append(float(request.form['X177']))
    my_list2 = np.asarray(my_list)
    

    DOWNLOAD_ROOT = "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    INFO_PATH = "00388"
    INFO_URL = DOWNLOAD_ROOT + INFO_PATH + "/data.csv"

    def fetch_info_data(info_url=INFO_URL,info_path=INFO_PATH):
        if not os.path.isdir(info_path):
            os.makedirs(info_path)
        file_path = os.path.join(info_path, "data.csv")
        urllib.request.urlretrieve(info_url,file_path)

    fetch_info_data()

        #Reading the downloaded file
    def load_info_data(info_path=INFO_PATH):
        csv_path = os.path.join(info_path, "data.csv")
        return pd.read_csv(csv_path)

    data = load_info_data()
    data = data.rename(index=str, columns={"Unnamed: 0": "ID"})
    #print(data)
    features = data.drop(['ID','y'],axis = 1)

    #log transformation
    features = features.transform(lambda x: np.log(x + 1 - min(x)))

    target = data['y']

    #feature selection
    attributes = ['X95', 'X101', 'X106', 'X111', 'X116', 'X121', 'X127', 'X144', 'X153',
       'X156', 'X160', 'X161', 'X169', 'X171', 'X177']

    features = features[attributes]

    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.2, random_state = 42,stratify = data['y'])

    #standarisation
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    #modelling
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(55, 50), random_state=1,early_stopping=True)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    
    cnf_matrix = confusion_matrix(y_test,y_pred)
    np.set_printoptions(precision=2)

    #reshaping the input
    my_list1 = my_list2.reshape(1, -1)
    #print(my_list1.shape)
    my_list1 = np.log(my_list1 + 1 - min(my_list1))
    #print(my_list1)
    my_list1 = sc.transform(my_list1)
    #print(my_list1)
    #print(my_list1)
    y_test_pred1 = clf.predict(my_list1)
    if y_test_pred1 == 1:
        y_test_pred1 = 'Recording of seizure activity'
    if y_test_pred1 == 2:
        y_test_pred1 = 'They record the EEG from the area where the tumor was located'
    if y_test_pred1 == 3:
        y_test_pred1 = 'Yes, They identify where the reason of the tumor was in the Brain and recording the EEG activity from the healthy brain area'
    if y_test_pred1 == 4:
        y_test_pred1 = 'Eyes closed, means when they were recording the EEG signal the patient had their eyes closed'
    if y_test_pred1 == 5:
        y_test_pred1 = 'Eyes open means when they were recording the EEG signal of the brain the patient had their eyes open'
    #print(y_test_pred1)

    recall1 = recall_score(y_test,y_pred, average='macro')*100
    recall = math.ceil(recall1*100)/100
    precision1 = precision_score(y_test,y_pred, average = 'macro')*100
    precision = math.ceil(precision1*100)/100
    flash("With Sensitivity : ")
    Sensitivity = recall
    flash("and Precision :")
    Precision = precision
    flash("The Status of Eplileptic Seizure Detection is:")
    y_test_pred2 = y_test_pred1



    return render_template("index.html",result = Sensitivity, result1 = Precision, result2 = y_test_pred2)


if __name__ == '__main__':
    app.run(debug = True, port = 5000)