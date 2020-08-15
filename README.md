# Loan-Prediction-
A demo project to elaborate the deployment of machine learning models on production using Flask API. This project is a part of my own study.
## Project Components-
This project has four major components:
XGBoost4.pkl:- This contains our machine learning model to predict the loan acceptance status based on training data set in 'train.csv'.

app.py:- This contains the backend of the project that is server using Flask APIs that recieves details through API calls, computes the predicted status based on our model and returns it.

Template:- This folder contains the fronted of the project using the HTML and CSS template to allow user to enter the values based on the trained model and displays the status of loan acceptance.

#### Running the project-
Ensure that you are in project home directory. Create the machine learning model by running below command
    python XGBoost4.py.
This would create a serialised version of our model into a file XGBoost4.pkl

Run app.py on command prompt using below command to start Flask API.
  python app.py
By default, flask will run on port 5000 which is your localhost.

Navigate to URL http://localhost:5000 you should be able to view the homepage as given in project.jpg file in repository.

Enter all the details asked on webpage properly and click Calculate the loan status button.

If your input is valid, you should be able to see the status of loan acceptance whether you can get or not below the the button.
