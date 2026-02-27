"""pbsparse module for reading in PBS Pro job records from accounting logs"""

from importlib.metadata import version, PackageNotFoundError
from .pbsparse import get_pbs_records, PbsRecord

__all__ = ["pbsparse"]

try:
    __version__ = version("pbsparse")
except PackageNotFoundError:
    # Fallback for development/uninstalled state if necessary
    __version__ = "0.0.0"
