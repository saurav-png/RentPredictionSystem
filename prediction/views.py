from django.shortcuts import render
#importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def home(request):
    return render(request,'prediction/index.html')

def result(request):
    
    def regression(user_value):
        global x_test,y_test,predictedval
        #Creating a dataframe of independent variables from the main df dataframe
        independent_var = df[["bedrooms", "bathrooms", "size_sqft", 
                        "min_to_subway", "floor", "building_age_yrs", 
                        "no_fee", "has_roofdeck", "has_washer_dryer", 
                        "has_doorman", "has_elevator", "has_dishwasher", 
                        "has_patio", "has_gym"]]

        #Creating a dataframe for dependent variable
        dependent_var = df[["rent"]]

        #Splitting independent variables into 80% training set and 20% testing set
        x_train, x_test, y_train,y_test = train_test_split(independent_var, dependent_var, train_size=0.8, test_size= 0.2, random_state=6)

        #Creating Liner Regression Model
        linmodel = LinearRegression()

        #Fitting in into the training stes
        linmodel.fit(x_train, y_train)

        predictedval = linmodel.predict(x_test)
        user_prediction = linmodel.predict(user_value)
        
        return user_prediction

    def predict():

        bedrooms =  float(request.GET.get('beds'))
        bathrooms =  float(request.GET.get('bath'))
        size_sqft =  float(request.GET.get('size'))
        min_to_subway =  float(request.GET.get('subway'))
        floor =  float(request.GET.get('floor-num'))
        building_age_yrs =  float(request.GET.get('buildingAge'))
        no_fee =  float(request.GET.get('broker-fee'))
        has_roofdeck =  float(request.GET.get('roof-deck'))
        has_washer_dryer =  float(request.GET.get('wash-drier'))
        has_doorman =  float(request.GET.get('doorman'))
        has_elevator =  float(request.GET.get('elevator'))
        has_dishwasher =  float(request.GET.get('dishwasher'))
        has_patio =  float(request.GET.get('patio'))
        has_gym =  float(request.GET.get('gym'))


        apartment_features = [bedrooms, bathrooms, size_sqft, min_to_subway, floor, building_age_yrs, no_fee, has_roofdeck, has_washer_dryer, has_doorman, has_elevator, has_dishwasher, has_patio, has_gym]
        arr = np.array(apartment_features, dtype=float).reshape(1,-1)

        predictedAmount = regression(arr)
        
        return predictedAmount

    def main():
        global search_location, df

        search_location = request.GET.get('city')
        df = pd.read_csv(f"prediction/streeteasy/{search_location}.csv")
        
        predictedAmount=predict()  # store the value from function (predict)
        return predictedAmount     # return the value to the function result

    predictedAmount=main()

    context = {
        'calculatedValue': predictedAmount,
        'showResult': True,
    }

    return render(request,'prediction/result.html',context)

def about(request):
    return render(request,'prediction/about.html')