# command line user interface for PyICMdump.py

import PyICMdump as icm

menu_str = 'Enter:\t [1] - Get current ICM forecast\t [2] - batch download forecasts from specified time range'
forecast_options_str = 'Select forecasts:\t no input - default(06:00 UTC),  00 - 00:00 UTC, 06 - 06:00 UTC, 12 - 12:00 UTC, 18 - 18:00 UTC, all - all'

# menu loop

# TODO: add exit option
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

        icd.dump()
    

