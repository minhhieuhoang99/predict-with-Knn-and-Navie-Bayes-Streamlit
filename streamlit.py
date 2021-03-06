import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler  
from sklearn.neighbors import KNeighborsClassifier
import plotly.express as px
from sklearn.naive_bayes import GaussianNB
# import module
import pandas as pd
# Get the Keys
def get_value(val,my_dict):
	for key ,value in my_dict.items():
		if val == key:
			return value

# Find the Key From Dictionary
def get_key(val,my_dict):
	for key ,value in my_dict.items():
		if val == value:
			return key 

def transform_gender(x):
    if x == 'Female':
        return 1
    elif x == 'Male':
        return 0
    else:
        return -1
    
def transform_customer_type(x):
    if x == 'Loyal Customer':
        return 1
    elif x == 'disloyal Customer':
        return 0
    else:
        return -1
    
def transform_travel_type(x):
    if x == 'Business travel':
        return 1
    elif x == 'Personal Travel':
        return 0
    else:
        return -1
    
def transform_class(x):
    if x == 'Business':
        return 2
    elif x == 'Eco Plus':
        return 1
    elif x == 'Eco':
        return 0    
    else:
        return -1
    
def transform_satisfaction(x):
    if x == 'satisfied':
        return 1
    elif x == 'neutral or dissatisfied':
        return 0
    else:
        return -1
    
def process_data(df):
    df = df.drop(['Unnamed: 0', 'id'], axis = 1)
    df['Gender'] = df['Gender'].apply(transform_gender)
    df['Customer Type'] = df['Customer Type'].apply(transform_customer_type)
    df['Type of Travel'] = df['Type of Travel'].apply(transform_travel_type)
    df['Class'] = df['Class'].apply(transform_class)
    df['satisfaction'] = df['satisfaction'].apply(transform_satisfaction)
    df['Arrival Delay in Minutes'].fillna(df['Arrival Delay in Minutes'].median(), inplace = True)
    
    return df

# Training KNN Classifier
@st.cache(suppress_st_warning=True)
def Knn_Classifier(X_train, X_test, y_train, y_test,knn_slider):
    knn = KNeighborsClassifier(n_neighbors=knn_slider)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    score = metrics.accuracy_score(y_test, y_pred) * 100
    report = classification_report(y_test, y_pred)

    return score, report, knn

# Training Naive-bayes
@st.cache(suppress_st_warning=True)
def Naive_bayes(X_train, X_test, y_train, y_test):
    gnb = GaussianNB()
    gnb_model = gnb.fit(X_train, y_train)
    y_pred = gnb_model.predict(X_test)
    score = metrics.accuracy_score(y_test, y_pred) * 100
    report = classification_report(y_test, y_pred)
    return score, report, gnb

def accept_user_data():
    # id = st.text_input("Enter the id number: ")
    Gender = st.selectbox('Gi???i t??nh',tuple(Gender_label.keys()))
    Customer_Type = st.selectbox('Kh??ch h??ng',tuple(Customer_Type_label.keys()))
    Age = st.slider ("Tu???i: ",7,100)
    Type_of_Travel = st.selectbox('Lo???i h??nh chuy???n bay',tuple(Type_of_Travel_label.keys()))
    Class = st.selectbox('H???ng v??',tuple(Class_label.keys()))
    Flight_Distance = st.slider("Kho???ng c??ch chuy???n bay:",30,5000)
    Inflight_wifi_service   = st.slider("????nh gi?? d???ch v??? wifi:",0,5)
    Departure_Arrival_time_convenient   = st.slider ("????nh gi?? ????? thu???n ti???n c???a th???i gian ??i/?????n: ",0,5)
    Ease_of_Online_booking  = st.slider ("????nh gi?? d???ch v??? ?????t v?? tr???c tuy???n: ",0,5)
    Gate_location   = st.slider ("????nh gi?? v??? tr?? c???ng bay: ",0,5)
    Food_and_drink  = st.slider ("????nh gi?? ????? ??n/u???ng: ",0,5)
    Online_boarding = st.slider ("????nh gi?? d???ch v??? tr???c tuy???n: ",0,5)
    Seat_comfort    = st.slider ("????nh gi?? gh??? ng???i: ",0,5)
    Inflight_entertainment  = st.slider ("????nh gi?? d???ch v??? gi???i tr??: ",0,5)
    On_board_service    = st.slider ("????ch gi?? d???ch v??? nh???n v?? tr???c tuy???n: ",0,5)
    Leg_room_service    = st.slider ("????nh gi?? ch??? ????? ch??n: ",0,5)
    Baggage_handling    = st.slider ("????nh gi?? v??? h??nh l?? x??ch tay: ",0,5)
    Checkin_service = st.slider ("????nh gi?? d???ch v??? checkin: ",0,5)
    Inflight_service    = st.slider ("????nh gi?? d???ch v??? tr??n chuy???n bay: ",0,5)
    Cleanliness = st.slider ("????nh gi?? v??? sinh chuy???n bay: ",0,5)
    Departure_Delay_in_Minutes  = st.slider ("Th???i gian kh???i h??nh mu???n: ",0,1200)
    Arrival_Delay_in_Minutes    = st.slider ("Th???i gian k???t th??c mu???n: ",0,1200)
    k_Gender = get_value(Gender,Gender_label)
    k_Customer_Type = get_value(Customer_Type,Customer_Type_label)
    k_Type_of_Travel = get_value(Type_of_Travel,Type_of_Travel_label)
    k_Class = get_value(Class,Class_label)
    user_prediction_data = np.array([Gender,Customer_Type,Age,Type_of_Travel,Class,Flight_Distance,Inflight_wifi_service,Departure_Arrival_time_convenient,Ease_of_Online_booking,Gate_location,Food_and_drink,Online_boarding,Seat_comfort,Inflight_entertainment,On_board_service,Leg_room_service,Baggage_handling,Checkin_service,Inflight_service,Cleanliness,Departure_Delay_in_Minutes,Arrival_Delay_in_Minutes]).reshape(1,-1)
    user_prediction_data_encode = np.array([k_Gender,k_Customer_Type,Age,k_Type_of_Travel,k_Class,Flight_Distance,Inflight_wifi_service,Departure_Arrival_time_convenient,Ease_of_Online_booking,Gate_location,Food_and_drink,Online_boarding,Seat_comfort,Inflight_entertainment,On_board_service,Leg_room_service,Baggage_handling,Checkin_service,Inflight_service,Cleanliness,Departure_Delay_in_Minutes,Arrival_Delay_in_Minutes]).reshape(1,-1)
    
    return user_prediction_data,user_prediction_data_encode

def load_print_data():
    # Insert Check-Box to show the snippet of the data.
    if st.checkbox('Hi???n th??? d??? li???u'):
        st.subheader("Hi???n th??? 100 d??ng d??? li???u---->>>") 
        st.write(df_train.head(100))
    # Insert Check-Box to show the snippet of the data.
    if st.checkbox('Hi???n th??? d??? li???u m?? h??a'):
        st.subheader("Hi???n th??? 100 d??ng d??? li???u m?? h??a---->>>") 
        st.write(train.head(100)) 
    

# assign dataset names
list_of_names = ['train','test']
# create empty list
dataframes_list = []
# append datasets into teh list
for i in range(len(list_of_names)):
    temp_df = pd.read_csv("./airline-passenger-satisfaction/"+list_of_names[i]+".csv")
    dataframes_list.append(temp_df) 
# @st.cache
# def loadData():
    
df_train = dataframes_list[0]
df_test = dataframes_list[1]
    

train = process_data(df_train)
test = process_data(df_test)

features = ['Gender', 'Customer Type', 'Age', 'Type of Travel', 'Class',
       'Flight Distance', 'Inflight wifi service',
       'Departure/Arrival time convenient', 'Ease of Online booking',
       'Gate location', 'Food and drink', 'Online boarding', 'Seat comfort',
       'Inflight entertainment', 'On-board service', 'Leg room service',
       'Baggage handling', 'Checkin service', 'Inflight service',
       'Cleanliness', 'Departure Delay in Minutes', 'Arrival Delay in Minutes']
target = ['satisfaction']

X_train = train[features]
y_train = train[target].to_numpy()
X_test = test[features]
y_test = test[target].to_numpy()
le = LabelEncoder()
y_test = le.fit_transform(y_test.flatten())
y_train =le.fit_transform(y_train.flatten())
# Normalize Features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

Gender_label = {'N???': 0, 'Nam': 1}
Customer_Type_label = {'Kh??ch h??ng th??n thi???t': 0, 'Kh??ch h??ng th?????ng': 1}
Type_of_Travel_label = {'C??ng t??c': 0, 'C?? nh??n': 1}
Class_label = {'Th????ng gia': 0, 'Th?????ng': 1, 'Ti???t ki???m': 2}
satisfaction_label = {'Ph??n v??n ho???c kh??ng H??i l??ng': 0, 'H??i l??ng': 1}
# Accepting user data for predicting its Member Type

def main():
           
    # ML Section
    choose_model = st.sidebar.selectbox("T??y Ch???n",["B??o C??o", "K-Nearest Neighbours" , "Navie-Bayes"])
    if(choose_model == "B??o C??o"):
        st.write("Ch??a C?? Chi ")

    if(choose_model == "Navie-Bayes"):
        st.title("D??? ??o??n s??? h??i l??ng c???a kh??ch h??ng v???i chuy???n bay s??? d???ng thu???t to??n Navie-Bayes")
        # X_train, X_test, y_train, y_test, le = process_data(df_train)
        score, report, gnb = Naive_bayes(X_train, X_test, y_train, y_test)
        st.text("????? ch??nh x??c c???a m?? h??nh Naive_bayes l??: ")
        st.write(score,"%")
        st.text("B??o c??o m?? h??nh Naive_bayes: ")
        st.write(report)
        lpd = load_print_data() 
        st.write(lpd)
        user_prediction_data , user_prediction_data_encode = accept_user_data()
        st.write(user_prediction_data)

        try:
            if(st.button(" D??? ??o??n ")):
                # user_prediction_data = accept_user_data()    
                pred = gnb.predict(user_prediction_data_encode)
                st.write("M?? h??a d??? li???u ????nh gi??: ", user_prediction_data_encode)
                # st.write("The Predicted Class is: ", pred) # Inverse transform to get the original dependent value.                
                final_result = get_key(pred,satisfaction_label)
                st.write("K???t qu??? d??? ??o??n")
                st.success(final_result) 
                if final_result =='Ph??n v??n ho???c kh??ng H??i l??ng':
                    st.write("Kh??ch h??ng ph??n v??n ho???c kh??ng h??i l??ng v??? chuy???n bay")
                if final_result =='H??i l??ng':
                    st.write("Kh??ch h??ng h??i l??ng v??? chuy???n bay")
        except:
            pass

    

    elif(choose_model == "K-Nearest Neighbours"):
        st.title("D??? ??o??n s??? h??i l??ng c???a kh??ch h??ng v???i chuy???n bay s??? d???ng thu???t to??n K-Nearest Neighbours")
        knn_slider  = st.slider("knn:",3, 101, 55, 2)
        if(knn_slider):
            score, report, knn = Knn_Classifier(X_train, X_test, y_train, y_test,knn_slider)
            st.write("????? ch??nh x??c c???a m?? h??nh K-Nearest Neighbour v???i k =",knn_slider," l??: ")
            st.write(score,"%")
            st.text("B??o c??o m?? h??nh K-Nearest Neighbour: ") 
            st.write(report)
            lpd = load_print_data()
            # knn_slider = st.slider("knn:",3, 101, 55, 2) 
            st.write(lpd)
            user_prediction_data , user_prediction_data_encode = accept_user_data()
            st.write(user_prediction_data)
        
        try:
            if(st.button(" D??? ??o??n ")):
                # user_prediction_data = accept_user_data()    
                pred = knn.predict(user_prediction_data_encode)
                st.write("M?? h??a d??? li???u ????nh gi??: ", user_prediction_data_encode)
                # st.write("The Predicted Class is: ", pred) # Inverse transform to get the original dependent value.                
                final_result = get_key(pred,satisfaction_label)
                st.write("K???t qu??? d??? ??o??n")
                st.success(final_result) 
                if final_result =='Ph??n v??n ho???c kh??ng H??i l??ng':
                    st.write("Kh??ch h??ng ph??n v??n ho???c kh??ng h??i l??ng v??? chuy???n bay")
                if final_result =='H??i l??ng':
                    st.write("Kh??ch h??ng h??i l??ng v??? chuy???n bay")
        except:
            pass

if __name__ == "__main__":
    main()