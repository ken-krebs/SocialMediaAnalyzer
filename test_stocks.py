from datetime import datetime
import stock_correlations as stock
import textwrap




def test_stock_data(capfd):
    date = datetime(2020, 4, 27, 2,22,00)
    response = "                 Open       High        Low  ...   Volume  Dividends  Stock Splits\nDate                                         ...                                  \n2020-04-27  21.450001  21.834999  21.140100  ...  5139599          0             0\n2020-04-27  21.629999  21.840000  21.535000  ...  2483514          0             0\n2020-04-27  21.753401  22.094999  21.700001  ...  2149571          0             0\n2020-04-27  21.992500  22.235001  21.980000  ...  2414510          0             0\n2020-04-27  22.219999  22.360001  22.150000  ...  2253494          0             0\n2020-04-27  22.230000  22.520000  22.230000  ...  2516624          0             0\n2020-04-27  22.514999  22.570000  22.400000  ...  2476058          0             0\n\n[7 rows x 7 columns]\n"
    stock.export_tweet_stock_correlations(date, 'GM') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data1(capfd):
    date = datetime(2020,10,12,2,5,46)
    response = ""
    stock.export_tweet_stock_correlations(date, 'TSLA') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data2(capfd):
    date = datetime(2018,7,19, 0,14,8)
    response = ""
    stock.export_tweet_stock_correlations(date, 'AMZN') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data3(capfd):
    date = datetime(2020,10,28, 14,19,43)
    response = ""
    stock.export_tweet_stock_correlations(date, 'TWTR') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data4(capfd):
    date = datetime(2020,9,26,15,31,58)
    response = ""
    stock.export_tweet_stock_correlations(date, 'TWTR') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data5(capfd):
    date = datetime(2019,11,4,21,38,52)
    response = ""
    stock.export_tweet_stock_correlations(date, 'SPOT') 
    out, err = capfd.readouterr()
    assert out == response

