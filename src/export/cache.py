

from pathlib import Path

CACHE_FOLDER = Path("data/cache")
CACHE_FOLDER.mkdir(parents=True, exist_ok=True)


def save_cache(gdf):
    gdf.to_parquet(CACHE_FOLDER / "municipalities.parquet")


def load_cache():
    path = CACHE_FOLDER / "municipalities.parquet"

    if path.exists():
        return path

    return None