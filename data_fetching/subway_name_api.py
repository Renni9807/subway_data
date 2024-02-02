import requests
from dotenv import load_dotenv
import os
import pickle
import redis

load_dotenv()

class KrSearchSTNBySubwayLineInfo : 
    def __init__(self):
        self.auth_key = os.getenv('API_KEY_KrSubwayNameAndLine')
                
    def start_first_work(self): # get all names of subway stations (Seoul)
        
        try:
            url = f"http://openapi.seoul.go.kr:8088/{self.auth_key}/json/SearchSTNBySubwayLineInfo/0/999/"
        
            response = requests.get(url)
            response.raise_for_status() # go to except block if error
            API_data_dict = response.json()
            data_needed = API_data_dict["SearchSTNBySubwayLineInfo"]["row"]        
            self.data_set = data_needed

            self.getInfoLineOne = [d for d in self.data_set if d.get('LINE_NUM') == '01호선']
            self.getInfoLineTwo = [d for d in self.data_set if d.get('LINE_NUM') == '02호선']
            self.getInfoLineThree = [d for d in self.data_set if d.get('LINE_NUM') == '03호선']
            self.getInfoLineFour = [d for d in self.data_set if d.get('LINE_NUM') == '04호선']
            self.getInfoLineFive = [d for d in self.data_set if d.get('LINE_NUM') == '05호선']
            self.getInfoLineSix = [d for d in self.data_set if d.get('LINE_NUM') == '06호선']
            self.getInfoLineSeven = [d for d in self.data_set if d.get('LINE_NUM') == '07호선']
            self.getInfoLineEight = [d for d in self.data_set if d.get('LINE_NUM') == '08호선']
            self.getInfoLineNine = [d for d in self.data_set if d.get('LINE_NUM') == '09호선']
            self.getInfoLineIncheon2 = [d for d in self.data_set if d.get('LINE_NUM') == '인천2호선']
            self.getInfoLineIncheon1 = [d for d in self.data_set if d.get('LINE_NUM') == '인천선']   # 인천1호선
            self.getInfoLineSuinBundang = [d for d in self.data_set if d.get('LINE_NUM') == '수인분당선']
            self.getInfoLineShinBundang = [d for d in self.data_set if d.get('LINE_NUM') == '신분당선']
            self.getInfoLineGyeongui = [d for d in self.data_set if d.get('LINE_NUM') == '경의선']
            self.getInfoLineGyeongchun = [d for d in self.data_set if d.get('LINE_NUM') == '경춘선']
            self.getInfoLineGyeonggang = [d for d in self.data_set if d.get('LINE_NUM') == '경강선']
            self.getInfoLineAirport = [d for d in self.data_set if d.get('LINE_NUM') == '공항철도']  # 공항
            self.getInfoLineWestCoast = [d for d in self.data_set if d.get('LINE_NUM') == '서해선']
            self.getInfoLineShillim = [d for d in self.data_set if d.get('LINE_NUM') == '신림선']    
            self.getInfoLineUiiNew = [d for d in self.data_set if d.get('LINE_NUM') == '우이신설경전철'] # 우이신설선
            self.getInfoLineUijeongbuLightRailway = [d for d in self.data_set if d.get('LINE_NUM') == '의정부경전철'] # 의정부
            self.getInfoLineGimpoUrbanRailway = [d for d in self.data_set if d.get('LINE_NUM') == '김포도시철도']    # 김포골드
        
        except requests.exceptions.RequestException as e:
            print("Error occurred during the HTTP requests:", str(e))
        except Exception as e:
            print("Error occurs:", str(e))
        # finally:
        #     print(response.status_code, "\n\n\n")    
        
    def start_second_work(self):
        line_nums = ['01호선', '02호선', '03호선', '04호선', '05호선', '06호선', '07호선', '08호선', '09호선', '인천2호선', '인천선', '수인분당선', '신분당선', '경의선', '경춘선', '경강선', '공항철도', '서해선', '신림선', '우이신설경전철', '의정부경전철', '김포도시철도']
        
        for line_num in line_nums:
            info_line = self.get_info_line(line_num)
            print(info_line)
            
    def get_info_line(self, line_num) -> list:
        return [d for d in self.data_set if d.get('LINE_NUM') == line_num]
            
    
    def connect_redis_server(self):
        try:
            r = redis.Redis(host='localhost', port=6379, decode_responses=True)
            self_str = pickle.dumps(self)  # pickle.dumps(self) --> serializes a python object hierarchy and returns the bytes object of the serialized object
            r.set('self', self_str)            
            
        except Exception as e:
            print("Error occurred while connecting to Redis server:", str(e))
    
work = KrSearchSTNBySubwayLineInfo()
work.start_first_work()
# work.start_second_work()
work.connect_redis_server()





