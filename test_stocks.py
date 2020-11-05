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
    response = "                  Open        High  ...  Dividends  Stock Splits\nDate                                ...                         \n2020-10-12  442.000000  445.850006  ...          0             0\n2020-10-12  441.385590  443.499786  ...          0             0\n2020-10-12  440.630005  443.700012  ...          0             0\n2020-10-12  443.290009  444.890015  ...          0             0\n2020-10-12  443.558807  448.440002  ...          0             0\n2020-10-12  448.140015  448.739990  ...          0             0\n2020-10-12  444.640015  444.700012  ...          0             0\n\n[7 rows x 7 columns]\n"
    stock.export_tweet_stock_correlations(date, 'TSLA') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data2(capfd):
    date = datetime(2018,7,19, 0,14,8)
    response = "- AMZN: 1h data not available for startTime=1531959248 and endTime=1532045648. The requested range must be within the last 730 days.\nEmpty DataFrame\nColumns: [Open, High, Low, Close, Adj Close, Volume]\nIndex: []\n"
    stock.export_tweet_stock_correlations(date, 'AMZN') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data3(capfd):
    date = datetime(2020,10,28, 14,19,43)
    response = "                 Open       High        Low  ...   Volume  Dividends  Stock Splits\nDate                                         ...                                  \n2020-10-28  49.599998  50.000000  48.660000  ...        0          0             0\n2020-10-28  49.029999  49.740002  48.950001  ...  2919294          0             0\n2020-10-28  49.099998  49.099998  48.330002  ...  3187615          0             0\n2020-10-28  48.570000  48.779999  48.251499  ...  2177151          0             0\n2020-10-28  48.680000  48.970001  48.520000  ...  1347363          0             0\n2020-10-28  48.919998  49.255001  48.550098  ...  1674628          0             0\n2020-10-28  49.209999  49.412701  48.500000  ...  2624937          0             0\n\n[7 rows x 7 columns]\n"
    stock.export_tweet_stock_correlations(date, 'TWTR') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data4(capfd):
    date = datetime(2020,9,26,15,31,58)
    response = "- TWTR: No data found for this date range, symbol may be delisted\nEmpty DataFrame\nColumns: [Open, High, Low, Close, Adj Close, Volume]\nIndex: []\n"
    stock.export_tweet_stock_correlations(date, 'TWTR') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data5(capfd):
    date = datetime(2019,11,4,21,38,52)
    response = "                  Open        High         Low  ...  Volume  Dividends  Stock Splits\nDate                                            ...                                 \n2019-11-05  151.669998  153.309998  150.000000  ...  838081          0             0\n2019-11-05  151.460007  152.729996  151.000000  ...  528637          0             0\n2019-11-05  152.589996  152.669998  151.175003  ...  263626          0             0\n2019-11-05  151.339996  151.720001  150.976898  ...  132484          0             0\n2019-11-05  151.419998  151.639999  150.914307  ...  129524          0             0\n2019-11-05  151.270004  151.410004  150.820007  ...  219093          0             0\n2019-11-05  150.904999  151.100006  150.360001  ...  258960          0             0\n\n[7 rows x 7 columns]\n"
    stock.export_tweet_stock_correlations(date, 'SPOT') 
    out, err = capfd.readouterr()
    assert out == response

