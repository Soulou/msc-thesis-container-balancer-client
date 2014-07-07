import datetime

def timestamp_to_time(timestamp):
    return datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%Y-%m-%d %H:%M:%S')

