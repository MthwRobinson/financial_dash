import os
import json
import quandl

class QuandlService():
    """
    Returns economic data from quandl
    """
    def __init__(self):
        """
        Finds the dictionary of economic data to return
        """
        # Finds the path to the services folder as opens
        #   the configuration file
        self.path = os.path.dirname(os.path.realpath(__file__))
        with open(self.path + '/quandl.json', 'r') as f:
            self.quandl_calls = json.load(f)

    def get_quandl(self, store = False, from_file = False):
        """
        Pulls the quandl data specified in the configuration
            file and converts it into a dictionary
        """
        # Load save results if from_file is set to true
        loaded = False
        if from_file:
            files = os.listdir(self.path)
            if 'quandl_results.json' in files:
                with open(self.path + '/quandl_results.json', 'r') as f:
                    data = json.load(f)
                if data:
                    loaded = True

        # If the data has not been loaded yet, pull it from quandl
        if not loaded:
            data = []
            for call in self.quandl_calls:
                # Return economic data from quandl as a dataframe
                df = quandl.get(call['quandlCode'])
                column_name = list(df.columns)[0]

                # Transform the data into a dictionary
                data.append({
                    'name' : call['name'],
                    'dates' : [str(x) for x in df.index],
                    'values' : [x for x in df[column_name]]
                })
        
        if store:
            with open(self.path + '/quandl_results.json', 'w') as f:
                json.dump(data, f)

        return data











