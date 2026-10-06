class BallPlayer:
	def __init__(self,name:str,number:int,goals:int,assists:int,minutes:int):
		self.name=name
		self.number=number
		self.goals=goals
		self.assists=assists
		self.minutes=minutes

	def __str__(self):
		return f"BallPlayer(name={self.name}, number={self.number}, goals={self.goals}, passes={self.assists}, minutes={self.minutes})"

def most_goals(ballplayers:list):
	giga_nigga=max(ballplayers, key=lambda ballplayer: ballplayer.goals)
	return giga_nigga.name

def most_points(ballplayers:list):
	giga_nigga=max(ballplayers, key=lambda ballplayer: ballplayer.goals+ballplayer.assists)
	return (giga_nigga.name,giga_nigga.number)

def least_minutes(ballplayers:list):
	giga_nigga=min(ballplayers,key=lambda ballplayer: ballplayer.minutes)
	return giga_nigga