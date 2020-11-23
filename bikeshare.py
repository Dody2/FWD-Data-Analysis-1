import time
import pandas as pd


# creating a dictionary for the data sources
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Create list for cities
    cities_list = ["chicago", "new york", "washington"]
    while True :
        # Try statement to handle exceptions
        try:
            city = int(input("Choose city integer you would like to see: 1- Chicago 2- New York 3- Washington. :\n"))
            # Check input then assign list value to city
            if city in range(1, len(cities_list) + 1):
                city = cities_list[city - 1]
                break
            else:
                print("\nInvalid number, Please Choose a number between 1 and 3.")
        except ValueError:
            print("\nWrong Value, Please Choose a number between 1 and 3.")


    # Get user input for month (all, january, february, ... , june)
    month_list = ["all", "january", "february", "march", "april", "may", "june"]
    while True:
        try:
            month = int(input("Choose a month integer from jan to june to filter by (e.g. jan is 1) or 0 for all month : \n"))
            if month in range(0, len(month_list)) :
                month = month_list[month]
                break
            else:
                print("\nInvalid number, Please Choose a number between 0 and 6.")
        except ValueError:
            print("\nWrong Value, Please Choose a number between 0 and 6.")

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = ["all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    while True:
        try:
            day = int(input("Choose an integer of day of week to filter by (e.g. Sunday is 1) or 0 for all days : \n"))
            if day in range(0, len(days_list)) :
                day = days_list[day]
                break
            else:
                print("\nInvalid number, Please Choose a number between 0 and 7.")
        except ValueError:
            print("\nWrong Value, Please Choose a number between 0 and 6.")

    print("Your Choices is {}, {}, {}.".format(city, month, day))
    print('-'*60)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data
    df=pd.read_csv(CITY_DATA[city])

    # Converting start time to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # Extract month and days to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    # Filter by month 
    if month != "all" :
        months = ["january", "february", "marc", "april", "may", "june"]
        month = months.index(month) + 1

        
        df = df[df["month"] == month]

    # Filter by day
    if day != "all" :
        df = df[df["day_of_week"] == day.title()]





    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    months = ["january", "february", "marc", "april", "may", "june"]
    common_month = int(df["month"].mode()[0])
    print("The Most Common Month is : {} \n".format(months[common_month - 1]))

    # Display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("The Most Common Day is: {} \n".format(common_day))

    # Display the most common start hour
    # First extract hour column
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print("The Most Common Hour is : {} ".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("The Most Common Start Station is : {}\n".format(common_start_station))

    # Display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("The Most Common End Station is : {}\n".format(common_end_station))

    # Display most frequent combination of start station and end station trip
    # First Concatenate start and end
    df["Both Stations"] = df["Start Station"] + " To " + df["End Station"]
    frequent_stations = df["Both Stations"].mode()[0]
    print("The Most Frequent Combination of Start and End Stations : {}\n".format(frequent_stations))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The Total Travel Time is : {}\n".format(total_travel_time))

    # Display mean travel time
    mean_time = df["Trip Duration"].mean()
    print("The Mean of The Travel Time is : {}\n".format(mean_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The Counts of User Types :\n{}\n".format(user_types))

    # Display counts of gender
    # Try statement to handle exception if there is no data
    try:
        gender_counts = df["Gender"].value_counts()
        print("The Counts of Gender :\n{}\n".format(gender_counts))
    except:
        print("There is no Gender Data For This Chosen City")


    # Display earliest, most recent, and most common year of birth
    # Same as gender
    try:
        earliest_birth = int(df["Birth Year"].min())
        recent_birth = int(df["Birth Year"].max())
        common_birth = int(df["Birth Year"].mode()[0])

        print("The Earliest Birth Year is :  {}".format(earliest_birth))
        print("The Most Recent Birth Year is :  {}".format(recent_birth))
        print("The Most Common Birth is :  {}".format(common_birth))
    except:
        print("There is no Birth Data For This Chosen City")
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def display_data(df):
    """
    asks user if wants to display raw data


    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    
    Returns:
        None
    """
    print('\nGetting Raw Data...\n')


    # loop to get right input
    accepted_answer = ["yes", "no"]
    while True:
        dis_data = input("Do you want to see raw data ? : yes or no.\n").lower() 
        if dis_data in accepted_answer:
            break
        else:
            print("\nWrong Choice, Please Choose yes or no.")
        
    # variable for index
    index = 0
    if dis_data == "yes":
        raw_data = df.iloc[index:index + 5]
        print(raw_data)
        # ask if user wants to view more
        while True:
            dis_data = input("Do you want to see more raw data ? : yes or no.\n")
            if dis_data == "yes":
                index += 5
                raw_data = df.iloc[index:index + 5]
                print(raw_data)
            elif dis_data == "no":
                break
            else:
                print("\nWrong Choice, Please Choose yes or no.")
    
    
    print('-'*40)





def main():
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)
        
        display_data(df)
        
        time_stats(df)
        
        station_stats(df)
        
        trip_duration_stats(df)
        
        user_stats(df)
        


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("\nExiting...")

            break


if __name__ == "__main__":
    main()
