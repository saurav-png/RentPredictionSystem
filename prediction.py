#importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import max_error, mean_absolute_percentage_error, mean_squared_error,r2_score
from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

    print('*' * 50, "\n")
    print("Accuracy Info", "\n")
    print("Max Error: ", max_error(y_test, predictedval))
    print("Mean Absolute Percentage Error: ", mean_absolute_percentage_error(y_test, predictedval))
    print("Mean Squared Error: ", mean_squared_error(y_test, predictedval))
    print("RMSE", np.sqrt(mean_squared_error(y_test, predictedval)))
    print("R2: ", r2_score(y_test, predictedval),"\n")

    # Cross Validation 
    print("Automating Calculation of RMSE using different random state hyperparameter", "\n")
    scores = cross_val_score(linmodel, x_train, y_train, scoring="neg_mean_squared_error", cv= 5, n_jobs= 1)

    rmse = np.sqrt(-scores)
    print("RMSE values: ", np.round(rmse, 2))
    print("RMSE average: ", np.mean(rmse), "\n")
    print('*' * 50)


    return user_prediction
    

def predict():

    bedrooms = input("Number of Beadrooms ")
    bathrooms = input("Number of Bathrooms ")
    size_sqft = input("Size (Sq Feet) ")
    min_to_subway = input("Subway Station (min) ")
    floor = input("Floor Number ")
    building_age_yrs = input("Building's Age (Years) ")
    no_fee = input("Has A Broker Fee (0/1) ")
    has_roofdeck = input("Has Roof Deck (0/1) ")
    has_washer_dryer = input("Has Wash Drier (0/1) ")
    has_doorman = input("Has Doorman (0/1) ")
    has_elevator = input("Has Elevator (0/1) ")
    has_dishwasher = input("Has Dishwasher (0/1) ")
    has_patio = input("Has patio (0/1) ")
    has_gym = input("Has Gym ")



    apartment_features = [bedrooms, bathrooms, size_sqft, min_to_subway, floor, building_age_yrs, no_fee, has_roofdeck, has_washer_dryer, has_doorman, has_elevator, has_dishwasher, has_patio, has_gym]
    arr = np.array(apartment_features, dtype=float).reshape(1,-1)

    print(type(arr))
    predict = regression(arr)
    print("\n", "Predicted rent: $%.2f" % predict)




def main():
    global search_location, df
    locations = ["manhattan", "brooklyn", "queens"]

    search_location = input("Enter a location for your apartment") 

    if search_location not in locations:
        print("Invalid Location")
    else:
        df = pd.read_csv(f"streeteasy/{search_location}.csv")
    
    predict()


main()

   
  
