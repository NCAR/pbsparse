import pytest, os, sys
from pbsparse import pbsparse
from datetime import datetime

def get_data_path():
    my_root = os.path.dirname(os.path.realpath(__file__))
    return f"{my_root}/records"
    
def test_time_filter():
    records = list(pbsparse.get_pbs_records(get_data_path(), time_filter = [datetime(2025, 6, 9, 18, 20), datetime(2025, 6, 9, 18, 50)]))
    assert records[0].id == "5300607.casper-pbs"
