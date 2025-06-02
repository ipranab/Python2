Write a Python program using a Time class to input a given time in 24-hour format and convert it
to a 12-hour format with AM/PM. The program should also validate time strings to ensure they are
in the correct HH:MM:SS format. Implement a method to check if the time is valid and return an
appropriate message

Ans- 
    import re
    class Time:
        def __init__(self,time_str):
            self.time_str=time_str

        def is_valid(self):
            return bool(re.match(r'^\d{2}:\d{2}:\d{2}$', self.time_str))

        def to_12_hour_format(self):
            if not self.is_valid():
                return "Invalid time format"

            h,m,s=map(int,self.time_str.split(':'))
            suffix="AM" if h<12 else "PM"
            h=h%12 or 12
            return f"{h:02}:{m:02}:{s:02} {suffix}"

    t=Time("13:30:45")
    print(t.to_12_hour_format())
