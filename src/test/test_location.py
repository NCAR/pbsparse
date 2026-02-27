import pytest, os, sys
from pbsparse import pbsparse
from datetime import datetime

def get_data_path():
    my_root = os.path.dirname(os.path.realpath(__file__))
    return f"{my_root}/records"
    
def test_offset():
    records = list(pbsparse.get_pbs_records(get_data_path(), type_filter = "E", offset = 1))
    assert len(records) == 1 and records[0].id == "5300407.casper-pbs"

def test_offset_reversed():
    records = list(pbsparse.get_pbs_records(get_data_path(), type_filter = "E", reverse = True, offset = 1))
    assert len(records) == 1 and records[0].id == "5300605.casper-pbs"

def test_offset_number():
    records = list(pbsparse.get_pbs_records(get_data_path(), offset = 1, number = 1))
    assert len(records) == 1 and records[0].id == "5300607.casper-pbs"
