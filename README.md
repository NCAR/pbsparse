# pbsparse
A library for loading and processing PBS Professional accounting records.

## Details
The PBS Professional scheduler stores *event* records for each created job in
plain-text files called accounting logs. While these records do not contain all
of the information presented in the `qstat` command, they provide a large subset
and are useful for gauging system usage patterns, debugging job issues, and
more.

PBS Pro does provide the `tracejob` command to query the accounting logs on the
command line.

This **pbsparse** library allows for easy loading of PBS Pro accounting records
into Python scripts for analysis. All of the difficult work of robustly parsing
each accounting record is handled for you.

## Installation

Simply install from PyPI using pip:

```shell
$ python3 -m pip install pbsparse
```

## Usage

The main interface to load records is the `get_pbs_records` function. For
example, if you wanted to get all jobs by their start record, you could use the
following:

```python
from pbsparse import get_pbs_records

job_starts = get_pbs_records("/pbs/accounting/20250301", type_filter = "S")
```

This function allows for extensive filtering options.

You can also use the `PbsRecord` class directly:

```python
from pbsparse import PbsRecord

with open("/pbs/accounting/20250301", "r") as pbs_file:
    for line in pbs_file:
        # Read data into object and process metadata
        record = PbsRecord(record, True)
        print(record)
```
