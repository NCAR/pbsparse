# pbshist
A library for loading and processing PBS Professional accounting records.

## Details
The PBS Professional scheduler stores *event* records for each created job in
plain-text files called accounting logs. While these records do not contain all
of the information presented in the `qstat` command, they provide a large subset
and are useful for gauging system usage patterns, debugging job issues, and
more.

PBS Pro does provide the `tracejob` command to query the accounting logs on the
command line.

Our **pbshist** library allows for easy loading of PBS Pro accounting records
into Python scripts for analysis. All of the difficult work of robustly parsing
each accounting record is handled for you.

## Installation

TBD

## Usage

TBD
