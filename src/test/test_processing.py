import pytest
from pbsparse import pbsparse

def test_E_processing():
    data = '04/16/2025 10:19:48;E;4413086.casper-pbs;user=vanderwb group=csgteam account="SCSG0001" project=_pbs_project_default jobname=vncs-default queue=vis ctime=1744817013 qtime=1744817013 etime=1744817013 start=1744817058 exec_host=casper15/3 exec_vnode=(casper15:ncpus=1:ngpus=1:mem=10485760kb) Resource_List.gpu_type=gp100 Resource_List.mem=10gb Resource_List.mps=0 Resource_List.ncpus=1 Resource_List.ngpus=1 Resource_List.nodect=1 Resource_List.nvpus=0 Resource_List.place=scatter Resource_List.select=1:ncpus=1:ngpus=1:os=opensuse15:ompthreads=1 Resource_List.walltime=04:00:00 session=45951 end=1744820388 Exit_status=271 resources_used.cpupercent=22 resources_used.cput=00:02:56 resources_used.mem=1243224kb resources_used.ncpus=1 resources_used.vmem=14088720kb resources_used.walltime=00:55:26 eligible_time=00:00:48 run_count=1'
    record = pbsparse.PbsRecord(data, True)
    assert record.resources_used["ncpus"] == 1

def test_R_processing():
    data = '04/15/2025 15:14:58;R;4400521.casper-pbs;user=rpconroy group=decs account="P43713000" project=_pbs_project_default jobname=dask-wk24-hpc queue=rda ctime=1744751276 qtime=1744751276 etime=1744751276 start=1744751695 exec_host=crhtc07/14 exec_vnode=(crhtc07:ncpus=1:mem=4194304kb) Resource_List.mem=4gb Resource_List.ncpus=1 Resource_List.ngpus=0 Resource_List.nodect=1 Resource_List.place=scatter Resource_List.select=1:ncpus=1:mem=4GB:ompthreads=1 Resource_List.walltime=10:00:00 session=0 end=1744751698 Exit_status=-3 resources_used.cpupercent=0 resources_used.cput=00:00:00 resources_used.mem=0b resources_used.ncpus=1 resources_used.vmem=0kb resources_used.walltime=00:00:00 eligible_time=00:00:13 run_count=21'
    record = pbsparse.PbsRecord(data, True)
    assert record.run_count == 21

def test_D_processing():
    data = '04/16/2025 16:44:35;D;4421332.casper-pbs;requestor=bneuman@casper-login1.hpc.ucar.edu'
    record = pbsparse.PbsRecord(data, True)
    assert record.request_server == "casper-login1.hpc.ucar.edu"

def test_A_processing():
    data = '04/14/2025 10:56:00;A;4386764.casper-pbs;Job deleted as result of dependency on job 4386762.casper-pbs'
    record = pbsparse.PbsRecord(data, True)
    assert record.comment == "Job deleted as result of dependency on job 4386762.casper-pbs"

def test_Y_processing():
    data = '04/08/2025 17:30:20;Y;S3011784.casper-pbs;requestor=Scheduler@casper-pbs.hpc.ucar.edu start=1744207200 end=1744241400 nodes=(casper25:ncpus=36:ngpus=4:mem=773849088kb) count=2900'
    record = pbsparse.PbsRecord(data, True)
    assert record.count == 2900

def test_a_processing():
    data = '04/02/2025 21:36:23;a;4237334.casper-pbs;Resource_List.select=1:mem=1GB'
    record = pbsparse.PbsRecord(data, True)
    assert record.Resource_List["select"] == "1:mem=1GB"

def test_C_processing():
    data = "01/30/2025 12:13:41;C;3632465.casper-pbs;"
    record = pbsparse.PbsRecord(data, True)
    assert record.comment == ""
