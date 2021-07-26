from configparser import ConfigParser


def get_config(filepath = None):
    # Function that allows us to get configuration values from another file

    # Assign ConfigParser to a variable
    config = ConfigParser()
 
    # Read file with configuration values
    config.read(filepath or 'carapi/app.ini')   

    # Return the config
    return config
