# Project: PyICMdump
#
# Created by Michal Lukaszewicz (remoteVoyager) at 2019-03-14
# mlukaszewicz2@gmail.com

import datetime, urllib.request, requests
from datetime import datetime, timedelta, date
from pathlib import Path
from io import BytesIO
from PIL import Image


class dumper:

    def __init__(self, forecast_time = None):
        self.start_date = None
        self.end_date = None

        self.forecasts_list = ['00', '06', '12', '18']

        if forecast_time is None:
            self.forecasts = ['06']
        elif forecast_time is 'all':
            self.forecasts = self.forecasts_list
        elif forecast_time in self.forecasts_list:
            self.forecasts = [ forecast_time ]
        else:
            raise ValueError('Nie ma takiej prognozy!')

    def set_dates(self, dates=None):

        if dates is not None:
            # allows for direct date selection
            self.start_date = datetime.strptime(dates[0], '%Y-%m-%d')
            self.end_date = datetime.strptime(dates[1], '%Y-%m-%d')
        else:
            print("Enter dates like \'YYYY-MM-DD\'\n")

            while True:
                try:
                    self.start_date = datetime.strptime(input("Enter start time: "), '%Y-%m-%d')
                    self.end_date = datetime.strptime(input("Enter end time: "), '%Y-%m-%d')
                    break
                except ValueError:
                    print("Incorrect date format.\n")

        assert self.start_date < self.end_date, "Start date must be earlier than end date"

    def dump(self):

        delta = self.end_date - self.start_date
        days = [(self.start_date + timedelta(i)) for i in range(delta.days + 1)]  # collects all dates form the period

        for day in days:

            # format day for use in path 
            str_day = day.strftime("%Y%m%d")
            
            # if not exists create destination directory
            dest_dir = (Path(__file__).resolve().parent / day.strftime("%Y_%m_%B"))
            try:
                dest_dir.mkdir()
            except FileExistsError:
                pass
            
            # download and save meteogram for every chosen forecast time
            for forecast in self.forecasts:

                # create url
                url = "http://www.meteo.pl/um/metco/mgram_pict.php?ntype=0u&fdate={}&row=406&col=250&lang=pl".format(str_day + forecast)

                # create final file path
                src = dest_dir / ("{}_{}.meteo.png".format(str_day, forecast))

                # download forecast
                resp = urllib.request.urlopen(url)
                respHtml = resp.read()
                binfile = open(src, "wb")

                # save forecast
                binfile.write(respHtml)
                binfile.close()

                print("Forecast for: " + day.strftime("%d %b %Y") + ' time: ' + forecast + " saved")


def get_current_forecast(show=True):
    # choose latest forecast
    # forecasts are released with 5 hour delay
    now_utc = datetime.utcnow()

    day = datetime.today()

    if now_utc.hour < 5:
        # forecast form 18:00 previous day
        day = day - timedelta(1)
        print(day)

        release = '18'

    elif now_utc.hour < 11:
        # forecast from 00:00
        release = '00'

    elif now_utc.hour < 17:
        # forecast from 6:00
        release = '06'

    elif now_utc.hour < 23:
        # forecast from 12:00
        release = '12'

    else:
        # forecast from 18:00
        release = '18'

    url = "http://www.meteo.pl/um/metco/mgram_pict.php?ntype=0u&fdate={}&row=406&col=250&lang=pl".format(
        day.strftime("%Y%m%d") + release)

    resp = requests.get(url)
    img = Image.open(BytesIO(resp.content))
    
    if show:
        print('Displaying forecast for: {}, time: {}'.format(day.strftime("%d.%m.%Y"), release))
        img.show()

    else:
        return img
