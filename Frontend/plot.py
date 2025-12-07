import matplotlib.pyplot as plt 
import seaborn as sns
import calendar

def average_delivery_time(df) : 
    return (f"Average Time {round(df['Time_taken(min)'].mean(),2)}")


def city_fastest_delivery_times(df): 

    city_times = df.groupby('City_of_order')['Time_taken(min)'].mean().sort_values().reset_index()

    # Fastest city
    fastest_city = city_times.loc[0,'City_of_order']
    fastest_time = city_times.loc[0,'Time_taken(min)']
    st1 = f"Fastest city: {fastest_city} with {round(fastest_time, 2)} minutes"

    # Slowest city
    slowest_city = city_times.iloc[-1]['City_of_order']
    slowest_time = city_times.iloc[-1]['Time_taken(min)']
    st2 = f"Slowest city: {slowest_city} with {round(slowest_time, 2)} minutes"

    # Message
    msg = f"As we can see, almost all cities have similar average times. {st1} & {st2}."
    # Plot
    plt.figure(figsize=(10,7))
    sns.barplot(data=city_times, x='City_of_order', y='Time_taken(min)', palette='coolwarm')
    plt.xticks(rotation=90)
    plt.title("Delivery Time for Each City")

    return plt.gcf(), msg



def day_with_highest_delivery(df):

    day_fast = df.groupby('Day')['Time_taken(min)'].mean().sort_values().reset_index()

    plt.figure(figsize=(10,7))
    sns.barplot(data=day_fast, x='Day', y='Time_taken(min)', palette='coolwarm')
    plt.xticks(rotation=90)
    plt.title("Delivery Time for Each Day")

    # Lowest day
    best_day = day_fast.loc[0,'Day']
    best_time = day_fast.loc[0,'Time_taken(min)']
    s1 = f"Lowest delivery time day: {best_day} with {round(best_time, 2)} minutes"

    # Highest day
    worst_day = day_fast.iloc[-1]['Day']
    worst_time = day_fast.iloc[-1]['Time_taken(min)']
    s2 = f"Highest delivery time day: {worst_day} with {round(worst_time, 2)} minutes"

    # Message
    msg = f"As we can see, there is a difference in average time: {s1}, {s2} and After Search Friday in india tend to have High Traffic."

    return plt.gcf(), msg


def month_delv(df):
    month_fast = df.groupby('Month_of_order')['Time_taken(min)'].mean().sort_values().reset_index()

    plt.figure(figsize=(10,7))
    sns.barplot(data=month_fast, x='Month_of_order', y='Time_taken(min)', palette='coolwarm')
    plt.xticks(rotation=90)
    plt.title("Delivery Time for Each Month")

    # Lowest month
    lowest_month = int(month_fast.loc[0,'Month_of_order'])
    lowest_time = month_fast.loc[0,'Time_taken(min)']
    s1 = f"Lowest Month in Delivery Time: {calendar.month_name[lowest_month]} with {round(lowest_time, 2)} minutes"

    # Highest month
    highest_month = int(month_fast.iloc[-1]['Month_of_order'])
    highest_time = month_fast.iloc[-1]['Time_taken(min)']
    s2 = f"Highest Month in Delivery Time: {calendar.month_name[highest_month]} with {round(highest_time, 2)} minutes"

    # Message
    msg = f'''As we can see, there is a difference in average time: {s1}, {s2} and
    after search October often includes major festivals such as Diwali (October/November).'''

    return plt.gcf(), msg
    

def type_order_delv(df):
    typeorder_fast=df.groupby('Type_of_order')['Time_taken(min)'].mean().sort_values().reset_index()

    plt.figure(figsize=(10,7))
    sns.barplot(data=typeorder_fast,x='Type_of_order',y='Time_taken(min)',palette='coolwarm')
    plt.xticks(rotation=90)
    plt.title("Delivery Time for Each  Type of Order")
    msg="As We Can See All Category of Order Almost Have The Same Average Delivering Time."
    return plt.gcf(),msg


def Vehicle_delv(df):
    vehicle_df = df.groupby(['Type_of_vehicle','Vehicle_condition'])['Time_taken(min)'].mean().sort_values().reset_index()

    plt.figure(figsize=(10,7))
    sns.barplot(data=vehicle_df, x='Type_of_vehicle', y='Time_taken(min)', palette='coolwarm', hue='Vehicle_condition')
    plt.xticks(rotation=90)
    plt.title("Delivery Time for Each Type of Vehicle and Its Condition")

    # Fastest vehicle
    fastest_idx = vehicle_df['Time_taken(min)'].idxmin()
    fastest_vehicle = vehicle_df.loc[fastest_idx, 'Type_of_vehicle']
    fastest_condition = vehicle_df.loc[fastest_idx, 'Vehicle_condition']
    fastest_time = vehicle_df.loc[fastest_idx, 'Time_taken(min)']

    # Slowest vehicle
    slowest_idx = vehicle_df['Time_taken(min)'].idxmax()
    slowest_vehicle = vehicle_df.loc[slowest_idx, 'Type_of_vehicle']
    slowest_condition = vehicle_df.loc[slowest_idx, 'Vehicle_condition']
    slowest_time = vehicle_df.loc[slowest_idx, 'Time_taken(min)']

    # Message for Streamlit
    msg = (
    f"Fastest Delivery: {fastest_vehicle} (Condition {fastest_condition}) with {round(fastest_time,2)} minutes with good condition.\n"
    f"Slowest Delivery: {slowest_vehicle} (Condition {slowest_condition}) with {round(slowest_time,2)} minutes with bad condition.\n"
    "This shows that we need to check vehicle condition continuously."
)


    return plt.gcf(), msg

def festival_delv(df):
    festival_df = df.groupby('Festival')['Time_taken(min)'].mean().sort_values().reset_index()

    plt.figure(figsize=(10,7))
    sns.barplot(data=festival_df, x='Festival', y='Time_taken(min)', palette='coolwarm')
    plt.xticks(rotation=90)
    plt.title("Delivery Time with Festival")

    # Delivery times
    festival_yes = festival_df.loc[festival_df['Festival']=='Yes', 'Time_taken(min)'].values[0]
    festival_no = festival_df.loc[festival_df['Festival']=='No', 'Time_taken(min)'].values[0]

    # Message for Streamlit
    msg = (
        f"Delivery Time During Festival: {round(festival_yes,2)} minutes\n"
        f"Delivery Time When There is No Festival: {round(festival_no,2)} minutes\n"
        "As we can see, the festival affects delivery time."
    )

    return plt.gcf(), msg


def res_num_delv(df):
    Res=df.groupby('Restaurant_number')['Time_taken(min)'].mean().sort_values().reset_index()

    plt.figure(figsize=(10,7))
    sns.barplot(data=Res,x='Restaurant_number',y='Time_taken(min)',palette='coolwarm')
    plt.xticks(rotation=90)
    plt.title("Delivery Time for Each  Restaurant")
    msg="As We Can See Almost All Resturant Have The Same Delivery Time."
    return plt.gcf(),msg

def type_of_city(df): 
    city_type = df.groupby('City')['Time_taken(min)'].mean().sort_values().reset_index()

    # Plot
    plt.figure(figsize=(10,7))
    sns.barplot(data=city_type, x='City', y='Time_taken(min)', palette='coolwarm')
    plt.xticks(rotation=90)
    plt.title("Delivery Time for Each City")

    # Get fastest (lowest mean time)
    fastest_city = city_type.iloc[0]['City']
    fastest_time = city_type.iloc[0]['Time_taken(min)']

    # Get slowest (highest mean time)
    slowest_city = city_type.iloc[-1]['City']
    slowest_time = city_type.iloc[-1]['Time_taken(min)']

    msg = (
        f"The fastest delivery is in **{fastest_city}** "
        f"with an average time of **{fastest_time:.2f} minutes**.\n"
        f"The slowest delivery is in **{slowest_city}** "
        f"with an average time of **{slowest_time:.2f} minutes**."
    )

    return plt.gcf(), msg

def month_over_time(df):
    month_fast=df.groupby('Month_of_order')['Time_taken(min)'].mean().sort_values().reset_index()

    plt.figure(figsize=(10,7))
    sns.lineplot(data=month_fast,x='Month_of_order', y='Time_taken(min)')
    plt.title("Average Delivery Time per Month")
    plt.xlabel("Month")
    plt.ylabel("Average Time (min)")
    msg = (
    "The analysis shows that performance across the months is not stable; "
    "delivery times fluctuate, being high in some months and lower in others."
)
    return plt.gcf(),msg
    

def weather_time(df):
    Weather = df.groupby('Weatherconditions')['Time_taken(min)'].mean().sort_values().reset_index()

    plt.figure(figsize=(10,7))
    sns.barplot(data=Weather, x='Weatherconditions', y='Time_taken(min)', palette='coolwarm')
    plt.xticks(rotation=90)
    plt.title("Delivery Time for Each Weather Condition")

    # Fastest (lowest time)
    fastest_weather = Weather.loc[0, 'Weatherconditions']
    fastest_time = Weather.loc[0, 'Time_taken(min)']

    # Slowest (highest time)
    slowest_weather = Weather.iloc[-1]['Weatherconditions']
    slowest_time = Weather.iloc[-1]['Time_taken(min)']

    s1 = f"Fastest Delivery: {fastest_weather} with {round(fastest_time, 2)} minutes."
    s2 = f"Slowest Delivery: {slowest_weather} with {round(slowest_time, 2)} minutes."

    msg = (
        f"As we can see, weather conditions significantly affect delivery time. "
        f"{s1} {s2}"
    )

    return plt.gcf(), msg


def rate_time(df):
    corr = df[['Delivery_person_Ratings','Time_taken(min)']].corr()
    sns.heatmap(corr, annot=True, cmap='Blues',vmin=-1)
    msg = (
    "Yes, there is a clear relationship between Delivery Person Rating and Time Taken. "
    "The relationship is inverse: higher delivery ratings are generally associated with lower delivery times."
)
    return plt.gcf(),msg

def multiple_del(df):
    multiple_deliveries = (df.groupby('multiple_deliveries')['Time_taken(min)'].mean().sort_values().reset_index())

    # Plot
    plt.figure(figsize=(10,7))
    sns.barplot(
        data=multiple_deliveries,
        x='multiple_deliveries',
        y='Time_taken(min)',
        palette='coolwarm'
    )
    plt.xticks(rotation=90)
    plt.title("Delivery Time for Multiple Deliveries")

    # Fastest (lowest time)
    fastest_count = multiple_deliveries.loc[0, 'multiple_deliveries']
    fastest_time = round(multiple_deliveries.loc[0, 'Time_taken(min)'], 2)

    # Slowest (highest time)
    slowest_count = multiple_deliveries.iloc[-1]['multiple_deliveries']
    slowest_time = round(multiple_deliveries.iloc[-1]['Time_taken(min)'], 2)

    # Message
    msg = (
    f"Fastest Delivery occurs when the delivery person has {int(fastest_count)} "
    f"other deliveries, taking **{fastest_time} minutes** on average.\n\n"
    f"Slowest Delivery occurs when they have {int(slowest_count)} "
    f"other deliveries, taking **{slowest_time} minutes** on average.\n\n"
    f"This indicates that **more multiple deliveries generally increase the delivery time**."
)

    return plt.gcf(), msg


def traffic_time(df):
    traffic = (df.groupby('Road_traffic_density')['Time_taken(min)'].mean().sort_values().reset_index())

    # Plot
    plt.figure(figsize=(10,7))
    sns.barplot(
        data=traffic,
        x='Road_traffic_density',
        y='Time_taken(min)',
        palette='coolwarm'
    )
    plt.xticks(rotation=90)
    plt.title("Delivery Time for Each Traffic Condition")

    # Fastest traffic condition (lowest avg time)
    fastest_cond = traffic.loc[0, 'Road_traffic_density']
    fastest_time = round(traffic.loc[0, 'Time_taken(min)'], 2)

    # Slowest traffic condition (highest avg time)
    slowest_cond = traffic.iloc[-1]['Road_traffic_density']
    slowest_time = round(traffic.iloc[-1]['Time_taken(min)'], 2)

    # Message
    msg = (
        f"Fastest Delivery occurs during **{fastest_cond}** traffic "
        f"with an average time of **{fastest_time} minutes**.\n\n"
        f"Slowest Delivery occurs during **{slowest_cond}** traffic "
        f"with an average time of **{slowest_time} minutes**.\n\n"
        f"This clearly shows that **higher traffic density leads to longer delivery times**."
    )

    return plt.gcf(), msg


def age_time(df):
    age = ( df.groupby('Delivery_person_Age')['Time_taken(min)'].mean().sort_values().reset_index())

    plt.figure(figsize=(10,7))
    sns.barplot(data=age,x='Delivery_person_Age',y='Time_taken(min)',palette='coolwarm')
    plt.xticks(rotation=90)
    plt.title("Delivery Time for Each  Delivery_person_Age")
    msg="There is a pattern Here Delivery person under 30 are faster Than over 30 !"
    return plt.gcf(),msg

def boxplot_time(df):
    sns.boxplot(x=df['Time_taken(min)'])
    msg='''It seems fine. There is a small number of outliers, but this can happen when several factors occur together,
such as festivals, high traffic, 
poor vehicle conditions, or bad weather.'''

    return plt.gcf(),msg






