hour, minute = map(int, input().split())
required_time = int(input())

result_minute = (minute + required_time) % 60
result_hour = hour + (minute + required_time) // 60
result_hour = result_hour % 24

print(result_hour, result_minute)
