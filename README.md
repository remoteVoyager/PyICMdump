# PyICMdump
This script downloads meteograms from given period

## Usage

Currently availible functionalities:

* _dumper_ class:

    Allows to download all forecasts from given time period.
    
* _get_current_forecast_ function:
 
    Retrieves newest availible forecast and displays it.

* _PyICMdump_cli.py_ serves as quick CLI, currently covers current forecast fetch and batch forecast download

* Executable _PyICMdump_cli.py_ availible in exec/build. Build with pyinstaller on Windows.
    
Future functionalities:

* argparse interace
* async download
* GUI
* more flexible setup
* option to use in other software

