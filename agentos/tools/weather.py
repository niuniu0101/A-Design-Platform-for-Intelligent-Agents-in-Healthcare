
class weather:
    def __init__(
        self,
        key:str = None,
        url:str = "https://restapi.amap.com/v3/weather/weatherInfo"
    ):
        self.key=key
        self.url=url

    def run(self,city:str):
        """
        weather:Get the weather forecast for a given city.

        Args:
            city(str): City name or city code.
        """
        self.url = "https://restapi.amap.com/v3/weather/weatherInfo"
        params = {
            'key': self.key,
            'city': city,
            'extensions': 'all' 
        }
        import requests
        response = requests.get(self.url, params=params)
        data = response.json()

        if response.status_code == 200:
            data = response.json()

            if data['count'] != '0' :
                info = ""
                for d in data['forecasts'][0]['casts']:
                    items = [f"{k}={v}" for k, v in d.items()]
                    items = ', '.join(items)
                    info = info + items + "\n"
             
                return info
            
            return f"Failed to retrieve {city} data.Please check if the city is correct."
        else:
            return f"Failed to retrieve weather data. Status code: {response.status_code}"
        

 