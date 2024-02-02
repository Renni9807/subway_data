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
        
    def get_instance_data(self):
        r = redis.Redis(host='localhost', port=6379)
        pickled_work = r.get('self')
        try:
            self.work = pickle.loads(pickled_work)
            
        except pickle.UnpicklingError:
            print("Can't unpickle the data.")
        
    def get_line_data(self, line, day, direction, attribute_name):
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
                
    def connect_redis_server(self):
        try:
            r = redis.Redis(host='localhost', port=6379, decode_responses=True)
            self_str = pickle.dumps(self)  # pickle.dumps(self) --> serializes a python object hierarchy and returns the bytes object of the serialized object
            r.set('subway_schedule', self_str)            
            
        except Exception as e:
            print("Error occurred while connecting to Redis server:", str(e))
        
data = KrSubwayScheduleOneToEight()
data.get_instance_data()

data.get_line_data(data.work.getInfoLineOne, data.WEEKDAY, data.UP_CLOCKWISE, "line_one_one_one")
data.get_line_data(data.work.getInfoLineOne, data.WEEKDAY, data.DOWN_ANTICLOCKWISE, "line_one_one_two")
data.get_line_data(data.work.getInfoLineOne, data.SATURDAY, data.UP_CLOCKWISE, "line_one_two_one")
data.get_line_data(data.work.getInfoLineOne, data.SATURDAY, data.DOWN_ANTICLOCKWISE, "line_one_two_two")
data.get_line_data(data.work.getInfoLineOne, data.SUNDAY_HOLIDAY, data.UP_CLOCKWISE, "line_one_three_one")
data.get_line_data(data.work.getInfoLineOne, data.SUNDAY_HOLIDAY, data.DOWN_ANTICLOCKWISE, "line_one_three_two")

data.get_line_data(data.work.getInfoLineTwo, data.WEEKDAY, data.UP_CLOCKWISE, "line_two_one_one")
data.get_line_data(data.work.getInfoLineTwo, data.WEEKDAY, data.DOWN_ANTICLOCKWISE, "line_two_one_two")
data.get_line_data(data.work.getInfoLineTwo, data.SATURDAY, data.UP_CLOCKWISE, "line_two_two_one")
data.get_line_data(data.work.getInfoLineTwo, data.SATURDAY, data.DOWN_ANTICLOCKWISE, "line_two_two_two")
data.get_line_data(data.work.getInfoLineTwo, data.SUNDAY_HOLIDAY, data.UP_CLOCKWISE, "line_two_three_one")
data.get_line_data(data.work.getInfoLineTwo, data.SUNDAY_HOLIDAY, data.DOWN_ANTICLOCKWISE, "line_two_three_two")

data.get_line_data(data.work.getInfoLineThree, data.WEEKDAY, data.UP_CLOCKWISE, "line_three_one_one")
data.get_line_data(data.work.getInfoLineThree, data.WEEKDAY, data.DOWN_ANTICLOCKWISE, "line_three_one_two")
data.get_line_data(data.work.getInfoLineThree, data.SATURDAY, data.UP_CLOCKWISE, "line_three_two_one")
data.get_line_data(data.work.getInfoLineThree, data.SATURDAY, data.DOWN_ANTICLOCKWISE, "line_three_two_two")
data.get_line_data(data.work.getInfoLineThree, data.SUNDAY_HOLIDAY, data.UP_CLOCKWISE, "line_three_three_one")
data.get_line_data(data.work.getInfoLineThree, data.SUNDAY_HOLIDAY, data.DOWN_ANTICLOCKWISE, "line_three_three_two")

data.get_line_data(data.work.getInfoLineFour, data.WEEKDAY, data.UP_CLOCKWISE, "line_four_one_one")
data.get_line_data(data.work.getInfoLineFour, data.WEEKDAY, data.DOWN_ANTICLOCKWISE, "line_four_one_two")
data.get_line_data(data.work.getInfoLineFour, data.SATURDAY, data.UP_CLOCKWISE, "line_four_two_one")
data.get_line_data(data.work.getInfoLineFour, data.SATURDAY, data.DOWN_ANTICLOCKWISE, "line_four_two_two")
data.get_line_data(data.work.getInfoLineFour, data.SUNDAY_HOLIDAY, data.UP_CLOCKWISE, "line_four_three_one")
data.get_line_data(data.work.getInfoLineFour, data.SUNDAY_HOLIDAY, data.DOWN_ANTICLOCKWISE, "line_four_three_two")

data.get_line_data(data.work.getInfoLineFive, data.WEEKDAY, data.UP_CLOCKWISE, "line_five_one_one")
data.get_line_data(data.work.getInfoLineFive, data.WEEKDAY, data.DOWN_ANTICLOCKWISE, "line_five_one_two")
data.get_line_data(data.work.getInfoLineFive, data.SATURDAY, data.UP_CLOCKWISE, "line_five_two_one")
data.get_line_data(data.work.getInfoLineFive, data.SATURDAY, data.DOWN_ANTICLOCKWISE, "line_five_two_two")
data.get_line_data(data.work.getInfoLineFive, data.SUNDAY_HOLIDAY, data.UP_CLOCKWISE, "line_five_three_one")
data.get_line_data(data.work.getInfoLineFive, data.SUNDAY_HOLIDAY, data.DOWN_ANTICLOCKWISE, "line_five_three_two")

data.get_line_data(data.work.getInfoLineSix, data.WEEKDAY, data.UP_CLOCKWISE, "line_six_one_one")
data.get_line_data(data.work.getInfoLineSix, data.WEEKDAY, data.DOWN_ANTICLOCKWISE, "line_six_one_two")
data.get_line_data(data.work.getInfoLineSix, data.SATURDAY, data.UP_CLOCKWISE, "line_six_two_one")
data.get_line_data(data.work.getInfoLineSix, data.SATURDAY, data.DOWN_ANTICLOCKWISE, "line_six_two_two")
data.get_line_data(data.work.getInfoLineSix, data.SUNDAY_HOLIDAY, data.UP_CLOCKWISE, "line_six_three_one")
data.get_line_data(data.work.getInfoLineSix, data.SUNDAY_HOLIDAY, data.DOWN_ANTICLOCKWISE, "line_six_three_two")

data.get_line_data(data.work.getInfoLineSeven, data.WEEKDAY, data.UP_CLOCKWISE, "line_seven_one_one")
data.get_line_data(data.work.getInfoLineSeven, data.WEEKDAY, data.DOWN_ANTICLOCKWISE, "line_seven_one_two")
data.get_line_data(data.work.getInfoLineSeven, data.SATURDAY, data.UP_CLOCKWISE, "line_seven_two_one")
data.get_line_data(data.work.getInfoLineSeven, data.SATURDAY, data.DOWN_ANTICLOCKWISE, "line_seven_two_two")
data.get_line_data(data.work.getInfoLineSeven, data.SUNDAY_HOLIDAY, data.UP_CLOCKWISE, "line_seven_three_one")
data.get_line_data(data.work.getInfoLineSeven, data.SUNDAY_HOLIDAY, data.DOWN_ANTICLOCKWISE, "line_seven_three_two")

data.get_line_data(data.work.getInfoLineEight, data.WEEKDAY, data.UP_CLOCKWISE, "line_eight_one_one")
data.get_line_data(data.work.getInfoLineEight, data.WEEKDAY, data.DOWN_ANTICLOCKWISE, "line_eight_one_two")
data.get_line_data(data.work.getInfoLineEight, data.SATURDAY, data.UP_CLOCKWISE, "line_eight_two_one")
data.get_line_data(data.work.getInfoLineEight, data.SATURDAY, data.DOWN_ANTICLOCKWISE, "line_eight_two_two")
data.get_line_data(data.work.getInfoLineEight, data.SUNDAY_HOLIDAY, data.UP_CLOCKWISE, "line_eight_three_one")
data.get_line_data(data.work.getInfoLineEight, data.SUNDAY_HOLIDAY, data.DOWN_ANTICLOCKWISE, "line_eight_three_two")

data.connect_redis_server()