hour, minute = map(int, input().split())
required_time = int(input())

hour += required_time // 60
minute += required_time % 60

if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24

print(hour, minute)
