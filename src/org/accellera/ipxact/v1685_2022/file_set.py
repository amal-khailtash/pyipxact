from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.file_set_type import FileSetType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class FileSet(FileSetType):
    """This element specifies a list of unique pathnames to files and directories.

    It may also include build instructions for the files. If compilation
    order is important, e.g. for VHDL files, the files have to be
    provided in compilation order.
    """

    class Meta:
        name = "fileSet"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
