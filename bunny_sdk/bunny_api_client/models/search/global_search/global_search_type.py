from enum import Enum

class GlobalSearchType(str, Enum):
    Cdn = "cdn",
    Storage = "storage",
    Dns = "dns",
    Script = "script",
    Stream = "stream",

