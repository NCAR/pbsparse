import pytest
from pbsparse import pbsparse

record_1n = '02/11/2026 20:12:21;E;2281314.casper-pbs;user=vanderwb group=csgteam account="SCSG0001" project=_pbs_project_default jobname=qcmd queue=htc ctime=1770865912 qtime=1770865912 etime=1770865912 start=1770865936 exec_host=crhtc65/24 exec_vnode=(crhtc65:ncpus=1:mem=10485760kb) Resource_List.mem=10gb Resource_List.mps=0 Resource_List.ncpus=1 Resource_List.ngpus=0 Resource_List.nodect=1 Resource_List.place=scatter Resource_List.select=1:ncpus=1:mem=10GB:ompthreads=1 Resource_List.walltime=01:00:00 session=0 end=1770865941 Exit_status=0 resources_used.cpupercent=6 resources_used.cput=00:00:00 resources_used.mem=3792kb resources_used.ncpus=1 resources_used.vmem=3792kb resources_used.walltime=00:00:01 eligible_time=00:00:26 run_count=1'
record_2n = '02/11/2026 20:16:47;E;2281981.casper-pbs;user=vanderwb group=csgteam account="SCSG0001" project=_pbs_project_default jobname=qcmd queue=htc ctime=1770866179 qtime=1770866179 etime=1770866179 start=1770866202 exec_host=crhtc67/13+crhtc70/17 exec_vnode=(crhtc67:ncpus=1:mem=10485760kb)+(crhtc70:ncpus=1:mem=10485760kb) Resource_List.mem=20gb Resource_List.mps=0 Resource_List.ncpus=2 Resource_List.ngpus=0 Resource_List.nodect=2 Resource_List.place=scatter Resource_List.select=2:ncpus=1:mem=10GB:ompthreads=1 Resource_List.walltime=01:00:00 session=31501 end=1770866207 Exit_status=0 resources_used.cpupercent=2 resources_used.cput=00:00:00 resources_used.mem=4580kb resources_used.ncpus=2 resources_used.vmem=4580kb resources_used.walltime=00:00:01 eligible_time=00:00:24 run_count=1'

def test_raw_record():
    data = record_1n
    record = pbsparse.PbsRecord(data, False)
    assert record._raw_record == record_1n

def test_get_nodes_1n():
    data = record_1n
    record = pbsparse.PbsRecord(data, False)
    assert record.get_nodes() == ['crhtc65']

def test_get_nodes_2n():
    data = record_2n
    record = pbsparse.PbsRecord(data, False)
    assert record.get_nodes() == ['crhtc67', 'crhtc70']
