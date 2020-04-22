import time
import pandas as pd
import numpy as np
import json

# These are the examined cities and their respective data files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Users are first asked which city they want to examine and then they can specify month(s) and day(s)
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #city = input('You can choose between Chicago, New York City, and Washingtion. Please enter a city you want to explore: ')
    while True:
        try:
            city = input('You can choose between Chicago, New York City, and Washington. Please enter a city you want to explore: ').lower() 
            if city == "chicago" or city == "new york city" or city == "washington":
                break
        except ValueError:
            pass
        print("That's not a valid city. You can choose between Chicago, New York City, and Washington. Please choose one: ")
      
    # TO DO: get user input for month (all, january, february, ... , june)
    # month = input('You can choose a month from January til June, or you can choose all by just hitting enter. Please enter a month you want to explore: ')
    while True:
        try:
            month = input('You can choose a month from January til June, or you can choose all by typing "all". Please enter a month you want to explore: ').lower() 
            if month == "january" or month == "february" or month == "march" or month == "april" or month == "may" or month == "june" or month == "all":
                break
        except ValueError:
            pass
        print('That\'s not a valid month. Select a month from January til June, or you can choose all by typing "all" Please choose one: ')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # day = input('You can choose a day from monday til sunday, or you can choose all by just hitting enter. Please enter a day you want to explore: ')
    while True:
        try:
            day = input('You can choose a day from Monday til Sunday, or you can choose all by typing "all". Please enter a day you want to explore: ').lower() 
            if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday" or day == "sunday" or day == "all":
                break
        except ValueError:
            pass
        print('That\'s not a valid day. Select a day from Monday til Sunday, or you can choose all by typing "all" Please choose one: ')
    
   
    
    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # extract month and day of week from End Time to create new columns
    df['month'] = df['End Time'].dt.month
    df['day'] = df['End Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df[ df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)
    
    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Most Popular Start Day:', popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("Most popular start station and end station : {}, {}"\
            .format(popular_start_end_station[0], popular_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total Travel Time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean Travel Time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Count of user types: ", user_counts)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        
        for index,gender_count   in enumerate(gender_counts):
            print("  {}: {}".format(gender_counts.index[index], gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
        # most earliest birth year
        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)    
        # most recent birth year
        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)   
        # most common birth year
        most_common_year = birth_year.mode()[0]
        print("The most common birth year:", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays the raw bikeshare data."""
    row_length = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5
    for i in range(0, row_length, 5):
        
        yes = input('\nDo you want to see the raw bikesahre data? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break

        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(json_row)

# This main function is responsible for executing all predefined function in the desired sequence    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
