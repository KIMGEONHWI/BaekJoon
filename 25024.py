def is_valid_time(x, y):
    return 0 <= x <= 23 and 0 <= y <= 59

def is_valid_date(x, y):
    days_in_month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if 1 <= x <= 12:
        return 1 <= y <= days_in_month[x]
    return False

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    time_result = "Yes" if is_valid_time(x, y) else "No"
    date_result = "Yes" if is_valid_date(x, y) else "No"
    print(f"{time_result} {date_result}")
