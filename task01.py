import shutil
import sys
from pathlib import Path


def copy_and_sort(src: Path, dst: Path) -> None:
    """
    Recursively copy files from src to dst sorted by extension.
    """
    for item in src.iterdir():
        try:
            if item.is_dir():
                copy_and_sort(item, dst)
            elif item.is_file():
                extension = item.suffix.lower().lstrip('.') or 'no_extension'
                target_dir = dst / extension
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target_dir / item.name)
        except PermissionError:
            print(f"Permission denied: {item}")
        except OSError as e:
            print(f"Error processing {item}: {e}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python task01.py <source_dir> [destination_dir]")
        return

    src = Path(sys.argv[1]).resolve()
    dst = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path('dist').resolve()

    if not src.exists() or not src.is_dir():
        print("Source directory does not exist or is not a directory.")
        return

    try:
        dst.mkdir(parents=True, exist_ok=True)
        copy_and_sort(src, dst)
        print(f"Files copied and sorted in {dst}")
    except OSError as e:
        print(f"Failed to create destination directory: {e}")


if __name__ == '__main__':
    main()