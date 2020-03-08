# command line user interface for PyICMdump.py

import PyICMdump as icm
import os, sys

menu_str = '\nEnter:\t [1] - Get current ICM forecast\t [2] - batch download forecasts from specified time range:\n: '
forecast_options_str = '\nSelect forecasts:\t no input - default(06:00 UTC),  00 - 00:00 UTC, 06 - 06:00 UTC, 12 - 12:00 UTC, 18 - 18:00 UTC, all - all\n: '


# file path for pyinstaller (Soviut: https://stackoverflow.com/a/404750)

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

print(application_path)
# menu loop
while True:

    usr_input = input(menu_str)

    if  usr_input == '1':
        icm.get_current_forecast()
    elif usr_input == '2':
        # TODO: fix forecast selection, currently all throws error

        #setup forecast options
        usr_input = input(forecast_options_str)
        icd = icm.dumper(usr_input)
        icd.set_dates()

        icd.dump(app_path=application_path)
    else:
        input('Press enter to close')
        break

