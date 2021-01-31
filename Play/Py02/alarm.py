"""
Write a script that given an hour and minutes by user input, prints at what time the alarm clock will ring, knowing that the current hour is hour and the current minutes are minutes. The clock goes off after 6 hour and 51 minutes.

"""

hour = int(input())
minutes = int(input())
t = hour * 60 + minutes + 6 * 60 + 51
a_hour = (t // 60) % 24
a_minutes = t  % 60
print(str(a_hour).rjust(2, '0') + ":" + str(a_minutes).rjust(2, '0'))