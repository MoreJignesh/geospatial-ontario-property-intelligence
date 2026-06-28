

from src.ingestion.inspect_gdb import inspect_gdb

gdb_path = (
    "data/raw/"
    "ONTARIO_LAND_COVER_Version_1_0_Geodatabase/"
    "ONTARIO_LAND_COVER_VERSION_1_0.gdb"
)

inspect_gdb(gdb_path)