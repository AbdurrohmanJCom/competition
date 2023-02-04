class atbor_1:
    def __init__(self, given_days):
        self.given_days = given_days

    def year_in(self):
        global year_ans
        year_ans = self.given_days // 365
        return year_ans    

    def weeks_in(self):
        global weeks_ans
        weeks_in = self.given_days - year_ans * 365
        weeks_ans =  weeks_in // 7
        return weeks_ans

    def days_in(self):
        days_in = self.given_days - weeks_ans * 7
        return self.given_days - year_ans * 365 - weeks_ans * 7





a = atbor_1(738)
print('years : ' , a.year_in())
print('weeks : ', a.weeks_in())
print('days : ', a.days_in())