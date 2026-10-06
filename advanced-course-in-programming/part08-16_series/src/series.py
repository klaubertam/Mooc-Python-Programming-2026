class Series:
    def __init__(self,title:str,seasons:str,genre:list):
        self.title=title
        self.seasons=seasons
        self.genre=genre
        self.ratelist=[]
        self.rating_sum=0
        self.average_rating=0
        self.numberofratings=0

    def rate(self,rating:int):
        if rating>0 and rating<6:
            self.ratelist.append(rating)
        self.rating_sum=sum(self.ratelist)
        self.numberofratings=len(self.ratelist)
        self.average_rating=(self.rating_sum/self.numberofratings)
    
    def __str__(self):
        genres=", ".join(self.genre)
        if self.average_rating==0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genres}\nno ratings"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genres}\n{self.numberofratings} ratings, average {self.average_rating:.1f} points"


def minimum_grade(rating: float, series_list: list):
    best_series_list=[]
    for series in series_list:
        if series.average_rating>=rating:
            best_series_list.append(series)
    return best_series_list

def includes_genre(genre: str, series_list: list):
    best_series_list=[]
    for series in series_list:
        if genre in series.genre:
            best_series_list.append(series)
    return best_series_list