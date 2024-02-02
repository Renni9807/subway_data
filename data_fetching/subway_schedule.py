import requests
from dotenv import load_dotenv
import os
import redis 
import pickle
from subway_name_api import KrSearchSTNBySubwayLineInfo

load_dotenv()

class KrSubwayScheduleOneToEight:
    
    WEEKDAY = 1
    SATURDAY = 2
    SUNDAY_HOLIDAY = 3
    UP_CLOCKWISE = 1
    DOWN_ANTICLOCKWISE = 2
    
    def __init__(self):
        self.auth_key = os.getenv('API_KEY_KrSubwayScheduleOneToEight')
        self.line_data = {}
        
    def connect_redis_server_get(self):
        r = redis.Redis(host='localhost', port=6379)
        pickled_work = r.get('self')
        try:
            self.work = pickle.loads(pickled_work)
            
        except pickle.UnpicklingError:
            print("Can't unpickle the data.")
        
    def line_data_api(self, line, day, direction, attribute_name):
        for data in line:
            try:
                url = f"http://openAPI.seoul.go.kr:8088/{self.auth_key}/json/SearchSTNTimeTableByIDService/0/400/{data['STATION_CD']}/{day}/{direction}/"
                response = requests.get(url)
                API_data_dict = response.json()
                data_needed = API_data_dict["SearchSTNTimeTableByIDService"]["row"]
                self.line_data[attribute_name] = data_needed
            
            except requests.exceptions.RequestException as e:
                print("Error occurred during the HTTP requests:", str(e))
            except Exception as e:
                print("Error occurs:", str(e))                
                
    def connect_redis_server_post(self):
        try:
            r = redis.Redis(host='localhost', port=6379, decode_responses=True)
            self_str = pickle.dumps(self)  # pickle.dumps(self) --> serializes a python object hierarchy and returns the bytes object of the serialized object
            r.set('subway_schedule', self_str)    
            print(self_str)        
            
        except Exception as e:
            print("Error occurred while connecting to Redis server:", str(e))
    
    def get_line_data(self):
        line_numbers = {
            'line_one': 'getInfoLineOne',
            'line_two': 'getInfoLineTwo',
            'line_three': 'getInfoLineThree',
            'line_four': 'getInfoLineFour',
            'line_five': 'getInfoLineFive',
            'line_six': 'getInfoLineSix',
            'line_seven': 'getInfoLineSeven',
            'line_eight': 'getInfoLineEight'
            # more lines would be added 
        }
        for line, attribute in line_numbers.items():
            for day_type in [data.WEEKDAY, data.SATURDAY, data.SUNDAY_HOLIDAY]:
                for direction in [data.UP_CLOCKWISE, data.DOWN_ANTICLOCKWISE]:
                    data.line_data_api(getattr(data.work, attribute), day_type, direction, f"{line}_{day_type}_{direction}")
    
data = KrSubwayScheduleOneToEight()
data.connect_redis_server_get()
data.get_line_data()
data.connect_redis_server_post()
