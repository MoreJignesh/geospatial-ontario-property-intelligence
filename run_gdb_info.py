import rasterio
from rasterio.io import MemoryFile
from rasterio.env import Env

gdb_path = (
    "data/raw/"
    "ONTARIO_LAND_COVER_Version_1_0_Geodatabase/"
    "ONTARIO_LAND_COVER_VERSION_1_0.gdb"
)

print("Trying to open GDB...")

try:
    with rasterio.open(gdb_path) as src:
        print(src.profile)
except Exception as e:
    print(e)