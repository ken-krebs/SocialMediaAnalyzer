import get_ceo_name as ceostock


def test_get_ceo_name():
    assert ceostock.get_ceo_name("AAPL") == "@tim_cook"
    assert ceostock.get_ceo_name("TSLA") == "@elonmusk"
    assert ceostock.get_ceo_name("TWTR") == "@jack"
    assert ceostock.get_ceo_name("PYPL") == "@Dan_Schulman"
    assert ceostock.get_ceo_name("PEP") == "@ramonlaguarta"
    assert ceostock.get_ceo_name("VZ") == "@hansvestberg"
    assert ceostock.get_ceo_name("GM") == "@mtbarra"
    assert ceostock.get_ceo_name("SPOT") == "@eldsjal"
    assert ceostock.get_ceo_name("AMZN") == "@jeffbezos"
    assert ceostock.get_ceo_name("FB") == "@finkd"
    assert ceostock.get_ceo_name("GOOGL") == "@sundarpichai"
    assert ceostock.get_ceo_name("BOX") == "@levie"
    assert ceostock.get_ceo_name("MSFT") == "@satyanadella"
    


    
