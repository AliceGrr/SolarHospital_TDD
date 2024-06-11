from enum import Enum


class CommandTypes(Enum):
    UNKNOWN = 0
    GET_STATUS = 1
    STATUS_DOWN = 2
    DISCHARGE = 3