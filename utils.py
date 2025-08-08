# utils.py

def convert_to_seconds(time_str):
    if isinstance(time_str, str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s
    return None
