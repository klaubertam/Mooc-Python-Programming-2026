class  WeatherStation:
    def __init__(self,name:str):
        self.__name=name
        self.__observation_list=[]
    def add_observation(self,observation: str):
        self.__observation_list.append(observation)
    def latest_observation(self):
        if len(self.__observation_list)>0:
            last=len(self.__observation_list)-1
            return self.__observation_list[last]
        else:
            return ""
    def number_of_observations(self):
        return len(self.__observation_list)
    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"

