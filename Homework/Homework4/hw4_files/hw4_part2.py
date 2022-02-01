import hw4_util

def daily():
    '''This is the function thats called when daily is chosen
        It starts by getting the list of all the states, then runs through them until the
        selected state is found. Then it saves that states list and finds the daily average of the state
        if the state isn't found then it prints the state was not found.'''
    lists = hw4_util.part2_get_week(week)
    state = input("Enter the state: ").upper()
    print(state)
    for statelist in lists:
        if statelist[0] == state.strip():
            statelist = statelist
            avg = (((statelist[2] + statelist[3] + statelist[4] + statelist[5] + statelist[6] + statelist[7] + statelist[8]) / 7) / statelist[1]) * 100000
            print("Average daily positives per 100K population: {:.01f}".format(avg))
            break
        else:pass
    if statelist[0] != state.strip():
            print("State {} not found".format(state))

def dailyavg(state):
    '''This is a similar function but just used when the average for a specific state is needed
        in a separate function'''
    lists = hw4_util.part2_get_week(week)
    for statelist in lists:
        if statelist[0] == state:
            statelist = statelist
            avg = (((statelist[2] + statelist[3] + statelist[4] + statelist[5] + statelist[6] + statelist[7] + statelist[8]) / 7) / statelist[1]) * 100000
            return(round(avg,1))
            break

def pct():
    '''The pct function is the function called when pct is chosen
        it is similar to daily in how it works but instead of finding the daily average,
        it finds the average positive % daily'''
    lists = hw4_util.part2_get_week(week)
    state = input("Enter the state: ").upper()
    print(state)
    for statelist in lists:
        if statelist[0] == state.strip():
            statelist = statelist
            avgpos = (statelist[2] + statelist[3] + statelist[4] + statelist[5] + statelist[6] + statelist[7] +statelist[8])
            avgneg = (statelist[2] + statelist[3] + statelist[4] + statelist[5] + statelist[6] + statelist[7] + statelist[8] + statelist[9] + statelist[10] + statelist[11] + statelist[12] + statelist[13] + statelist[14] + statelist[15])
            totavg = (avgpos / avgneg) * 100
            print("Average daily positive percent: {:.01f}".format(totavg))
            break
        else:pass
    if statelist[0] != state.strip():
        print("State {} not found".format(state))

def pctavg(state):
    '''This is the same function but used in the high func when a specific state is needed.'''
    lists = hw4_util.part2_get_week(week)
    for statelist in lists:
        if statelist[0] == state:
            statelist = statelist
            avgpos = (statelist[2] + statelist[3] + statelist[4] + statelist[5] + statelist[6] + statelist[7] +statelist[8])
            avgneg = (statelist[2] + statelist[3] + statelist[4] + statelist[5] + statelist[6] + statelist[7] + statelist[8] + statelist[9] + statelist[10] + statelist[11] + statelist[12] + statelist[13] + statelist[14] + statelist[15])
            totavg = (avgpos / avgneg) * 100
            return(round(totavg,1))
            break

def quar():
    '''This function is called when quar is chosen
        It checks the daily average and percent avg and sees if they are considered a high risk state.
        Then it adds the state to a list which is given to the the print_abbreviations function which formats and prints them out.'''
    lists = hw4_util.part2_get_week(week)
    states = []
    for statelist in lists:
        daily = dailyavg(statelist[0])
        pct = pctavg(statelist[0])
        if daily > 10 or pct > 10:
            states.append(statelist[0])
    print("Quarantine states:")
    hw4_util.print_abbreviations(states)

def high():
    '''The last function is high and checks which is the state with the highest infection rate.
        I use 2 lists to hold the state name and avg infection, then I check all of the states and replace the state if it is
        a higher rate.'''
    lists = hw4_util.part2_get_week(week)
    states = [0]
    avges = [0]
    for statelist in lists:
        daily = dailyavg(statelist[0])
        if daily > avges[0]:
            states[0]=(statelist[0])
            avges[0] = daily
    print("State with highest infection rate is", states[0])
    print("Rate is {} per 100,000 people".format(avges[0]))

if __name__ == "__main__":
    while True:
        '''THis is the main loop that is running and calling the funcitons that need to be called.
            It also asks for the week and request. I was going to use __name__ == "__Main__" but its not a loop so I couldnt
            use the continue command to pass through the itteration.'''
        print("...")
        week = int(input("Please enter the index for a week: "))
        print(week)
        if week < 0:
            exit()
        elif week > 29:
            print("No data for that week")
            continue
        request = input("Request (daily, pct, quar, high): ")
        print(request)
        if "daily" in request.lower():
            daily()
        elif "pct" in request.lower():
            pct()
        elif "quar" in request.lower():
            quar()
        elif "high" in request.lower():
            high()
        else:
            print("Unrecognized request")
            continue