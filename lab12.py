class Time:
    def __init__(self,seconds):
        self.sec=seconds
    
    def convert_to_minutes(self):
        minutes=self.sec//60
        seconds=self.sec%60
        return(f"{minutes}:{seconds:02d}")
    def convert_to_hours(self):
        hours=self.sec//3600
        remaining=self.sec%3600
        minutes=remaining//60
        seconds=remaining%60
        return (f" {hours}:{minutes:02d}:{seconds:02d}")
seconds=int(input("Enter time in seconds : "))
t=Time(seconds)
print("coverted to minutes: ",t.convert_to_minutes())
print("Converted to hours : ",t.convert_to_hours())