import requests
import json

class kr_subway_timeTaken : 
    def __init__(self):
        self.auth_key = "446279734c72656e35354c4b575771"
        
        
    def start_work_first(self): # get all names of subway stations (Seoul)
        
        url = f"http://openapi.seoul.go.kr:8088/{self.auth_key}/json/SearchSTNBySubwayLineInfo/1/1000/"
        
        response = requests.get(url)
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
        
        # print(self.getInfoLineOne)
        # print("\n\n\n")
        # print(self.getInfoLineTwo)
        # print("\n\n\n")
        # print(self.getInfoLineThree)
        # print("\n\n\n")
        # print(self.getInfoLineFour)
        # print("\n\n\n")
        # print(self.getInfoLineFive)
        # print("\n\n\n")
        # print(self.getInfoLineSix)
        # print("\n\n\n")
        # print(self.getInfoLineSeven)
        # print("\n\n\n")
        # print(self.getInfoLineEight)
        # print("\n\n\n")
        # print(self.getInfoLineNine)
        # print("\n\n\n")
        # print(self.getInfoLineSuinBundang)
        # print("\n\n\n")
        # print(self.getInfoLineGyeongui)
        # print("\n\n\n")
        # print(self.getInfoLineIncheon2)
        # print("\n\n\n")
        # print(self.getInfoLineIncheon1)
        # print("\n\n\n")
        # print(self.getInfoLineGyeongchun)
        # print("\n\n\n")
        # print(self.getInfoLineGyeonggang)
        # print("\n\n\n")
        # print(self.getInfoLineAirport)
        # print("\n\n\n")
        # print(self.getInfoLineShillim)
        # print("\n\n\n")
        # print(self.getInfoLineWestCoast)
        # print("\n\n\n")
        # print(self.getInfoLineUiiNew)
        # print("\n\n\n")
        # print(self.getInfoLineUijeongbuLightRailway)
        # print("\n\n\n")
        # print(self.getInfoLineGimpoUrbanRailway)
        # print("\n\n\n\n\n")
        # print(len(self.getInfoLineOne))
        # print("\n\n\n")
        # print(len(self.getInfoLineTwo))
        # print("\n\n\n")
        # print(len(self.getInfoLineThree))
        # print("\n\n\n")
        # print(len(self.getInfoLineFour))
        # print("\n\n\n")
        # print(len(self.getInfoLineFive))
        # print("\n\n\n")
        # print(len(self.getInfoLineSix))
        # print("\n\n\n")
        # print(len(self.getInfoLineSeven))
        # print("\n\n\n")
        # print(len(self.getInfoLineEight))
        # print("\n\n\n")
        # print(len(self.getInfoLineNine))
        # print("\n\n\n")
        # print(len(self.getInfoLineSuinBundang))
        # print("\n\n\n")
        # print(len(self.getInfoLineGyeongui))
        # print("\n\n\n")
        # print(len(self.getInfoLineIncheon2))
        # print("\n\n\n")
        # print(len(self.getInfoLineShinBundang))
        # print("\n\n\n")
        # print(len(self.getInfoLineIncheon1))
        # print("\n\n\n")
        # print(len(self.getInfoLineGyeongchun))
        # print("\n\n\n")
        # print(len(self.getInfoLineGyeonggang))
        # print("\n\n\n")
        # print(len(self.getInfoLineAirport))
        # print("\n\n\n")
        # print(len(self.getInfoLineShillim))
        # print("\n\n\n")
        # print(len(self.getInfoLineWestCoast))
        # print("\n\n\n")
        # print(len(self.getInfoLineUiiNew))
        # print("\n\n\n")
        # print(len(self.getInfoLineUijeongbuLightRailway))
        # print("\n\n\n")
        # print(len(self.getInfoLineGimpoUrbanRailway))
        
        
    def start_work_second(self):    # get only name and line
        
        self.target_keys = ["STATION_NM", "STATION_NM_ENG", "STATION_NM_CHN", "STATION_NM_JPN", "LINE_NUM"]
        
        self.target_dict_LineOne = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineOne]
        self.target_dict_LineTwo = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineTwo]
        self.target_dict_LineThree = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineThree]
        self.target_dict_LineFour = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineFour]
        self.target_dict_LineFive = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineFive]
        self.target_dict_LineSix = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineSix]
        self.target_dict_LineSeven = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineSeven]
        self.target_dict_LineEight = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineEight]
        self.target_dict_LineNine = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineNine]
        self.target_dict_LineIncheon2 = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineIncheon2]
        self.target_dict_LineIncheon1 = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineIncheon1]
        self.target_dict_LineSuinBundang = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineSuinBundang]
        self.target_dict_LineShinBundang = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineShinBundang]
        self.target_dict_LineGyeongui = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineGyeongui]
        self.target_dict_LineGyeongchun = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineGyeongchun]
        self.target_dict_LineGyeonggang = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineGyeonggang]
        self.target_dict_LineAirport = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineAirport]
        self.target_dict_LineWestCoast = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineWestCoast]
        self.target_dict_LineShillim = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineShillim]
        self.target_dict_LineUiiNew = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineUiiNew]
        self.target_dict_LineUijeongbuLightRailway = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineUijeongbuLightRailway]
        self.target_dict_LineGimpoUrbanRailway = [{key: entry[key] for key in self.target_keys} for entry in self.getInfoLineGimpoUrbanRailway]
        
        print(self.target_dict_LineAirport, "\n\n\n", self.target_dict_LineGyeonggang)
     
             

work = kr_subway_timeTaken()
work.start_work_first()
work.start_work_second()



