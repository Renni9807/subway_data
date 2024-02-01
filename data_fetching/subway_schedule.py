import requests
from dotenv import load_dotenv
import os
import redis 
import pickle
from subway_name_api import KrSearchSTNBySubwayLineInfo

load_dotenv()

class KrSubwayScheduleOneToEight:
    
    def __init__(self):
        self.auth_key = os.getenv('API_KEY_KrSubwayScheduleOneToEight')
        
    def get_instance_data(self):
        r = redis.Redis(host='localhost', port=6379)
        pickled_work = r.get('self')
        try:
            work = pickle.loads(pickled_work)
            
            print(work)
        except pickle.UnpicklingError:
            print("Can't unpickle the data.")
        
    def start_work(self):
        pass
        url = f"http://openAPI.seoul.go.kr:8088/(인증키)/xml/SearchSTNTimeTableByIDService/1/5/0309/1/1/"
        
        
data = KrSubwayScheduleOneToEight()
data.get_instance_data()
