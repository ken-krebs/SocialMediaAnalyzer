from datetime import datetime
import stock_correlations as stock
import textwrap




def test_stock_data(capfd):
    date = datetime(2020, 4, 27, 2,22,00)
    response = "             Open   High    Low  Close   Volume  Dividends  Stock Splits\nDate                                                                    \n2020-04-27  21.45  21.83  21.14  21.64  5139599          0             0\n2020-04-27  21.63  21.84  21.53  21.75  2483514          0             0\n2020-04-27  21.75  22.09  21.70  21.99  2149571          0             0\n2020-04-27  21.99  22.24  21.98  22.21  2414510          0             0\n2020-04-27  22.22  22.36  22.15  22.23  2253494          0             0\n2020-04-27  22.23  22.52  22.23  22.51  2516624          0             0\n2020-04-27  22.51  22.57  22.40  22.45  2476058          0             0\n"
    stock.export_tweet_stock_correlations(date, 'GM') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data1(capfd):
    date = datetime(2020,10,12,2,5,46)
    response = "              Open    High     Low   Close    Volume  Dividends  Stock Splits\nDate                                                                         \n2020-10-12  442.00  445.85  438.58  441.38  10737080          0             0\n2020-10-12  441.39  443.50  439.06  440.74   4851762          0             0\n2020-10-12  440.63  443.70  439.67  443.20   4138947          0             0\n2020-10-12  443.29  444.89  441.88  443.58   3908974          0             0\n2020-10-12  443.56  448.44  443.25  448.14   5314825          0             0\n2020-10-12  448.14  448.74  443.18  444.65   5372609          0             0\n2020-10-12  444.64  444.70  441.51  442.00   2937245          0             0\n"
    stock.export_tweet_stock_correlations(date, 'TSLA') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data2(capfd):
    date = datetime(2018,7,19, 0,14,8)
    response = "- AMZN: 1h data not available for startTime=1531973648 and endTime=1532060048. The requested range must be within the last 730 days.\nEmpty DataFrame\nColumns: [Open, High, Low, Close, Adj Close, Volume]\nIndex: []\n"
    stock.export_tweet_stock_correlations(date, 'AMZN') 
    out, err = capfd.readouterr()
    assert out == response

def test_stock_data3(capfd):
    date = datetime(2020,10,28, 14,19,43)
    response = "             Open   High    Low  Close    Volume  Dividends  Stock Splits\nDate                                                                     \n2020-10-28  48.68  48.97  48.52  48.92         0          0             0\n2020-10-28  48.92  49.26  48.55  49.22   1674628          0             0\n2020-10-28  49.21  49.41  48.50  48.56   2624937          0             0\n2020-10-29  51.95  52.06  50.72  51.58  11426924          0             0\n2020-10-29  51.60  52.05  50.57  51.78   5857772          0             0\n2020-10-29  51.80  52.48  51.50  52.06   5368852          0             0\n2020-10-29  52.07  52.62  51.84  52.59   6908498          0             0\n"
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
    response = "              Open    High     Low   Close  Volume  Dividends  Stock Splits\nDate                                                                       \n2019-11-05  151.67  153.31  150.00  151.40  838081          0             0\n2019-11-05  151.46  152.73  151.00  152.68  528637          0             0\n2019-11-05  152.59  152.67  151.18  151.34  263626          0             0\n2019-11-05  151.34  151.72  150.98  151.39  132484          0             0\n2019-11-05  151.42  151.64  150.91  151.27  129524          0             0\n2019-11-05  151.27  151.41  150.82  150.92  219093          0             0\n2019-11-05  150.90  151.10  150.36  150.47  258960          0             0\n"
    stock.export_tweet_stock_correlations(date, 'SPOT') 
    out, err = capfd.readouterr()
    assert out == response

