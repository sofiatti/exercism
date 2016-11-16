from datetime import datetime, timedelta

def add_gigasecond(birthdate):
    gigasecond = 10**9
    date = birthdate + timedelta(0, gigasecond)
    return date