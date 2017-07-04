from financial_dash.services.quandl import QuandlService

def test_quandl():
    """
    Tests the format of the quandl service calll
    """
    qs = QuandlService()

    # Pull down data from quandl and store/test the result
    data = qs.get_quandl(store = True)
    for result in data:
        assert type(result['name']) == str
        assert type(result['dates']) == list
        assert type(result['values']) == list
        assert len(result['values']) == len(result['dates'])

    # Pull data from the stored file and test the result
    data = qs.get_quandl(from_file = True)
    for result in data:
        assert type(result['name']) == str
        assert type(result['dates']) == list
        assert type(result['values']) == list
        assert len(result['values']) == len(result['dates'])

