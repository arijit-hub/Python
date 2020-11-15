def airplane_arrival(arrival_time,estimated_time):
    
    '''(number,number)->str

    Returns if a flight is on time or early or delayed from arrival_time and estimated_time

    Pre-condition: 0.0<=arrival_time<24 and 0.0<=estimated_time<24
    >>>airplane_arrival(1,0.5)
    'Delay'
    '''

    if arrival_time==estimated_time:
        return 'on time'

    elif arrival_time>estimated_time:
        return 'delayed'

    else:
        return 'early'
