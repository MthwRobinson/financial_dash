import dash
import dash_core_components as dcc
import dash_html_components as html

class NewsTable():
    def __init__(self):
        """
        Initiates the table of headlines
        """
        self.headlines = [{
            'title' : 'Headline ' + str(i+1),
            'date' : '2017-07-04'
        } for i in range(10)]
        self.div = self.generate_table()


    def generate_table(self):
        """
        Generates the table object
        """
        header = html.Tr([
            html.Th('Headline'),
            html.Th('Date')
        ])

        rows = [header]
        for headline in self.headlines:
            rows.append(html.Tr([
                html.Td(headline['title']),
                html.Td(headline['date'])
            ]))

        table = html.Table(rows)

        return table


