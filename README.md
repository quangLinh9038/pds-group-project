# Project Name
This project is a submission of COSC2789: Assignment 3- Group Project on Classification evaluating Spotify's Popular Songs from 2000-2020

#### -- Project Status: [Completed]

## Project Intro/Objective
The purpose of this project is evaluate dataset to build approriate models which can be used for deployed API severs. These models are aimed to predict song archived from Spotify in the period of 2000-2020, will be popular or not. 

### Partner
* Lecturer: Vo Ngoc Yen Nhi
* Kaggle Dataset: provided by Yamaç Eren Ay


#### Other Members:
* Nguyen Quang Linh - s3697110
* Nguyen Thanh Dat - s3697822
* Nguyen Quang Huy - s3697272
* Le Gia Thuan - s3695519

### Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling

### Technologies

* Python
* Pandas, jupyter notebook, numpy, sklearn
* pickle, dash
* sns, matplotlib


## Follow libraries requiremnt [requirements](Link to file)

## Visualize dataset with Dash dashboard
==================================

Dash can be installed with (also pandas is required for loading dataset): 
```
pip install dash
```

Run Terminal CMD or Powershell in Anaconda Navigator:
```
cd /your_local_file/Dash/your_python_app
```

To run dashboard type:
```
python app.py
```

## Run API models
==================================
Run Terminal CMD or Powershell command: 

```
cd /your_local_file/app.py
```

Run: 
```
python app.py
```

- app.py will run on http://127.0.0.1:5000

Using Postman application to test API:

Postman header setting

```
Content-Type: application/json
Accept: application/json
```


Predict: API will take the test set and output predicted values with the route "/predict"

```
http://127.0.0.1:5000/predict
```

Evaluate: API will take the test set and output evaluated values with the route "/evaluate"

```
http://127.0.0.1:5000/evaluate
```


