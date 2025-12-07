import streamlit as st 
import pandas as pd
from plot import *
import joblib
st.set_page_config(
    page_title="Food Delivery Project",
    page_icon="🍔",
    layout="wide",   # <- This makes it full width
    initial_sidebar_state="auto"
)

st.title("Food Delivery Project 🍔")

tab1,tab2 ,tab3 ,tab4,tab5 ,tab6=st.tabs(["Data","Analsis"," Recomendations","Test Modling","Score Metrics","About Me"])


import os
df_path = os.path.join(os.path.dirname(__file__), "../Data/Cleaned_Train.csv")
df = pd.read_csv(df_path)

test_model_performace= os.path.join(os.path.dirname(__file__), "../Note_Books/test_models_data.csv")
model_df = pd.read_csv(test_model_performace)
with tab1:

    # Add CSS for Kaggle-style lines with thin borders
    st.markdown("""
    <style>
    .kline {
        font-size: 17px;
        padding: 6px 0;
        border-bottom: 0.5px solid #2f2f2f;  /* subtle thin border */
    }

    .key {
        font-weight: 600;
        color: #e5e5e5;
    }

    .value {
        color: #bdbdbd;
        margin-left: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.subheader("📖 About Dataset")
    
    st.markdown("""
Food delivery is a courier service in which a restaurant, store, or independent food-delivery company delivers food to a customer. 
An order is typically made either through a restaurant or grocer's website or mobile app, or through a food ordering company. 
The delivered items can include entrees, sides, drinks, desserts, or grocery items and are typically delivered in boxes or bags. 
The delivery person will normally drive a car, but in bigger cities where homes and restaurants are closer together, they may use bikes or motorized scooters.  
This dataset represents **food delivery operations in India  (Metric : r2 Score)**.
""")
    
    st.markdown("### 📘 Dataset Overview")

    # Kaggle-style key-value lines
    columns_info = {
        "ID": "Unique ID for each order",
        "City": "City category where the order happened",
        "Delivery_person_ID": "ID of the delivery driver",
        "Delivery_person_Age": "Age of delivery person",
        "Delivery_person_Ratings": "Driver rating score",
        "Restaurant_latitude": "Latitude of restaurant",
        "Restaurant_longitude": "Longitude of restaurant",
        "Delivery_location_latitude": "Latitude of customer area",
        "Delivery_location_longitude": "Longitude of customer area",
        "Order_Date": "Date when the order was placed",
        "Time_Orderd": "Time order was created",
        "Time_Order_picked": "Time driver picked the order",
        "Weatherconditions": "Weather at delivery time",
        "Road_traffic_density": "Traffic conditions",
        "Vehicle_condition": "Condition rating of vehicle",
        "Type_of_order": "Type of food ordered",
        "Type_of_vehicle": "Vehicle used for delivery",
        "multiple_deliveries": "Number of deliveries at once",
        "Festival": "Festival day indicator",
        "Time_taken(min)": "Total delivery duration in minutes"
    }

    for key, value in columns_info.items():
        st.markdown(
            f"<div class='kline'><span class='key'>{key} :</span>"
            f"<span class='value'>{value}</span></div>",
            unsafe_allow_html=True
        )


with tab6:
        st.subheader("👤 About Me")

        st.markdown("""
    <style>
    .profile-card {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #333;
        color: #e5e5e5;
        line-height: 1.6;
    }
    </style>

    <div class="profile-card">
    <b>Name:</b> Fathy Abderabbo<br>
    <b>Education:</b> Undergraduate Student, Faculty of Engineering, Mansoura University<br>
    <b>Major:</b> Computer and Control Dept (CCSED)<br>
    <b>Expected Graduation:</b> July 2027<br>
    <b>Role/Interest:</b> Data Scientist & Machine Learning Engineer
    </div>
    """, unsafe_allow_html=True)




with tab2:
        select_box = st.selectbox(
            label="Choose Graph",
            options=[
                'City Vs Time', 'Age Vs Time', 'Rate Vs Time', 'Day vs Time',
                'Festival Vs Time','Type of Order Vs Time','Month Vs Time','Type of City Vs Time','Vehicle Vs Time',
                'Resturnat number Vs Time','Weather Vs Time','Traffic Vs Time',
                'Box plot of Time', 'Multiple Delveriy Vs Time','Performace Over Months'
            ]
        )

        graph_functions = {
            'City Vs Time': city_fastest_delivery_times,
            'Age Vs Time': age_time,
            'Rate Vs Time': rate_time,
            'Day vs Time': day_with_highest_delivery,
            'Festival Vs Time': festival_delv,
            'Type of Order Vs Time': type_order_delv,
            'Type of City Vs Time' : type_of_city,
            'Month Vs Time': month_delv,
            'Resturnat number Vs Time': res_num_delv,
            'Weather Vs Time': weather_time,
            'Traffic Vs Time': traffic_time,
            'Vehicle Vs Time' :Vehicle_delv,
            'Box plot of Time': boxplot_time,
            'Multiple Delveriy Vs Time': multiple_del,
            'Performace Over Months': month_over_time
        }

        # Call the function and get both figure and message
        fig, message = graph_functions[select_box](df)

        # Display
        st.pyplot(fig)
    
        if  st.button("Check Message"):
            st.write("Button pressed!")  # confirms click
            st.markdown(f"**📢 Note:** {message}")


    
        
with tab5:
    st.header("Metrics of Different Models on Test Data")
    st.table(model_df)

    #top 3 models
    top_models = model_df['Model-Name'].head(3).tolist()

    # Display top models after grid search
    st.markdown(
        f"""
        <h3 style='color:#1E90FF;'>
        After performing Hyperparameter Tuning using Grid Search to find the best model:<br>
        <b>Top 3 Models:</b> {', '.join(top_models)}
        </h3>
        """,
        unsafe_allow_html=True
    )

    #  best R2 score
    st.markdown(
    """
    <h3 style='color:#FFA500;'>
    After performing Hyperparameter Tuning on the XGBoost model,  
    I obtained an (R² Score) of <b>94.7% on Test Data set</b>.
    </h3>
    """,
    unsafe_allow_html=True
)
with tab4:
        
        @st.cache_data
        def pre_process_model(input_data):
            # Load preprocessor and model
            preprocessor = joblib.load('Note_Books/preprocessor.pkl')
            model = joblib.load('Note_Books/xgb_model_full_feature.pkl')

            # Transform input and predict
            transformed = preprocessor.transform(input_data)
            predicted = model.predict(transformed)
            return predicted

        # ---------------- Layout: Centered Form ----------------
        left, center, right = st.columns([1, 4, 1])  # Center width = 4

        with center:
            with st.form("delivery_prediction_form"):
                st.markdown(
                    "<h1 style='color:#1E90FF; font-size:20px;'>Enter Delivery Data:</h1>",
                    unsafe_allow_html=True
                )

                # ---------------- Input Fields ----------------
                age = st.number_input("Delivery Person Age", min_value=18, max_value=50, value=25, step=1)
                rating = st.number_input("Delivery Person Ratings", min_value=0.0, max_value=5.0, value=3.0, step=0.1)
                Weatherconditions = st.radio("Weather Condition", ['sunny', 'cloudy', 'fog', 'stormy', 'windy'])
                Vehicle_condition = st.selectbox("Vehicle Condition",[0,1,2,3])
                Road_traffic_density = st.radio("Road Traffic Density", ['High', 'Medium', 'Low'])
                Type_of_order = st.selectbox("Type of Order", ["Meal", "Snack", "Drinks", "Buffet"])
                Type_of_vehicle = st.selectbox("Type of Vehicle", ["motorcycle", "bicycle", "electric_scooter","scooter"])
                multiple_deliveries = st.selectbox("Multiple Deliveries", [0, 1, 2, 3])
                Festival = st.radio("Festival", ['Yes', 'No'])
                City_of_order = st.selectbox(
                    "Customer City Name",
                    ['Indore','Bangalore','Coimbatore','Chennai','Hyderabad','Ranchi','Mysore','Delhi','Kochi',
                    'Pune','Ludhiana','Kanpur','Mumbai','Kolkata','Jaipur','Surat','Aurangabad','Agra','Vadodara','Aligarh','Bhopal']
                )
                City = st.radio("Type of City", ['Urban', 'Metropolitan', 'Semi-Urban'])
                Restaurant_number = st.number_input("Restaurant ID", min_value=1, max_value=13, value=7)
                Delivery_person_number = st.number_input("Delivery Person ID", min_value=1, max_value=3, value=1)
                Day_of_order = st.selectbox("Day of Order", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
                Month_of_order = st.selectbox("Month of Order", list(range(1, 13)))
                Day = st.number_input("Day Number (1–31)", min_value=1, max_value=31, value=5)
                preparing_order = st.number_input("Order Preparation Time (minutes)", min_value=1, max_value=120, value=10)
                Distance_From_Res_to_customer = st.number_input(
                    "Distance from Restaurant to Customer (km)", min_value=0.1, max_value=27.0, value=2.0, step=0.1
                )

                # ---------------- Submit Button ----------------
                submitted = st.form_submit_button("Predict Delivery Time")

                if submitted:
                    # ---------------- Build Input DataFrame ----------------
                    input_df = pd.DataFrame([{
                        "Delivery_person_Age": age,
                        "Delivery_person_Ratings": rating,
                        "Weatherconditions": Weatherconditions,
                        "Road_traffic_density": Road_traffic_density,
                        "Vehicle_condition": Vehicle_condition,
                        "Type_of_order": Type_of_order,
                        "Type_of_vehicle": Type_of_vehicle,
                        "multiple_deliveries": multiple_deliveries,
                        "Festival": Festival,
                        "City": City,
                        "City_of_order": City_of_order,
                        "Restaurant_number": Restaurant_number,
                        "Delivery_person_number": Delivery_person_number,
                        "Day_of_order": Day,
                        "Month_of_order": Month_of_order,
                        "Day": Day_of_order,
                        "preparing_order": preparing_order,
                        "Distance_From_Res_to_customer": Distance_From_Res_to_customer
                    }])
                    
                    # ---------------- Predict ----------------
                    prediction = pre_process_model(input_df)
                    st.success(f"Predicted Delivery Time: {prediction[0]:.2f} minutes")
                    st.balloons()


        
        # Index(['Delivery_person_Age', 'Delivery_person_Ratings', 'Weatherconditions',
    #    'Road_traffic_density', 'Vehicle_condition', 'Type_of_order',
    #    'Type_of_vehicle', 'multiple_deliveries', 'Festival', 'City',
    #    'City_of_order', 'Restaurant_number', 'Delivery_person_number',
    #    'Day_of_order', 'Month_of_order', 'Day', 'preparing_order',
    #    'Distance_From_Res_to_customer']

with tab3 :
    st.header("Delivery Time Report")
    st.markdown("""
                <h3>
                
                Delivery time is influenced by many factors, which can be divided into two main categories:
                <br>
                ### <u>1. Factors We Cannot Control</u>
                - Weather conditions  
                - Festivals and public events  
                - Road traffic levels  
                - Distance between the restaurant and the customer  
                - Specific days like Fridays where demand or traffic is unusually high 
                - Type of City if it is Urban , Semi-Urban or Metropolitan 

                <br>

                ### <u>2. Factors We Can Control</u>
                - **Age of the delivery person:** Drivers under 30 consistently deliver faster  
                - **Driver rating:** Higher-rated drivers tend to complete deliveries quicker  
                - **Vehicle type & condition:**  
                - Motor Cycle  show the fastest performance When it is in  Condition  1
                - Vehicles in * Good condition To perform better  
                - **Number of simultaneous deliveries:** Multiple deliveries at once significantly increase delivery time  

                <br>

                ### <u>Performance Trends</u>
                Monthly performance fluctuates and does not show a strong upward or downward trend.

                <br>

                ### <u>Recommendations</u>
                - Collect additional data on **customer satisfaction** to understand expectations better  
                - Ensure regular maintenance so vehicles remain in **condition 2 or 3**  
                - Increase usage of **electric bicycles**, as they provide the fastest delivery times  
                - Prefer hiring delivery personnel aged **20–30** with **high performance ratings**

                </h3>
                """, unsafe_allow_html=True)
    
    