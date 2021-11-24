import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities =['Chicago', 'New York City','Washington']
    city=[]
    while city not in cities:
        city=input('Please choose and type the name of one of the following cities: Chicago, New York City, Washington: ')
        city =city.lower().title()
        if city not in cities:
            print('Oops it seems like you mispelled the name of the city\n')

    print(city)
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    month=[]
    while month not in months:
        month=input('Please type the name of the month (januari-june,or all) of which you want to explore the data: ')
        month=month.lower()
        if month not in months:
            print('Oops it seems like you mispelled the name of the month\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday','all']
    day=[]
    while day not in days:
        day=input('Please type the name of the day (or "all") of which you want to explore the data: ')
        day=day.lower()
        if day not in days:
            print('Oops it seems like you mispelled the name of the month\n')


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

    df=pd.read_csv(city.lower().replace(' ','_')+'.csv')

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday

    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day = days.index(day) + 1
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    # TO DO: display the most common month
    print(df.head(7))
    print(df['month'].mode())
    month=df['month'].mode()[0]


    print('the most common month in the selected data is {}.'.format(months[month-1]))

    # TO DO: display the most common day of week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    day=df['day'].mode()[0]

    print('the most common day in the selected data is {}.'.format(days[day-1]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour = df['hour'].mode()[0]
    #print(df['hour'].mode())
    print('the most common hour in the selected data is {}.'.format(hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print('The most popular start station in the selected data is: {}'.format(start_station))


    # TO DO: display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print('The most popular start station in the selected data is: {}'.format(end_station))

    df['COMBO']=df['Start Station']+'-'+df['End Station']
    combo=df['COMBO'].mode()[0]
    # TO DO: display most frequent combination of start station and end station trip
    print('The most popular station combination in the selected data is: {}'.format(combo))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['travel time']=df['End Time']-df['Start Time']
    # TO DO: display total travel time
    print('Total travel time in selected data was: {}'.format(np.sum(df['travel time'])))


    # TO DO: display mean travel time
    print('Mean travel time in selected data was: {}'.format(np.mean(df['travel time'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    customer = df['User Type'][df['User Type']=='Customer'].count()
    sub = df['User Type'][df['User Type']=='Subscriber'].count()
    # TO DO: Display counts of user types
    print('Within the selected data were {} customers and {} subscribers.'.format(customer,sub))


    # TO DO: Display counts of gender
    try:
        male = df['Gender'][df['Gender']=='Male'].count()
        female = df['Gender'][df['Gender']=='Female'].count()
        print('Within the selected data were {} males and {} females.'.format(male,female))
    except:
        print('There is no gender data in the data selected')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        early = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print('The earliest, most recent and most common birth year in the selected data were: {}, {} and {}.'.format(early,recent,common))
    except:
        print('There is no birth year data in the data selected')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty:
            print('No data available for the time period and place selected')
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            raw_data = input('would you like to see 5 rows of raw data?')
            count=5
            while raw_data == 'yes':
                if count < df.shape[0]:
                    print(df.iloc[count-5:count,:])
                    count+=5
                else:
                    count=5
                raw_data = input('would you like to scroll down?')
                if raw_data !='yes':
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
