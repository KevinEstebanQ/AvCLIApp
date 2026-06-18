
from db.init_db import init_db
from data_import.batch_import import import_from_csv
from pathlib import Path
import csv
from db.seed import seed_assignment_types
def main():
    init_db()
    seed_assignment_types()

    path = Path(__file__).resolve().parent / "data_import"
    path_dir: dict[int, Path] = dict()
    count=0
    for f in path.iterdir():
        path_dir[count] = f
        count+=1
    print("select (1,2,3, etc..) the csv file to parse...")
    for k,v in path_dir.items():
        print(f"{k} --- {"".join(v.as_posix().split("/")[-1])}")
    selection = int(input())
    selected_path = path_dir.get(selection, None)
    if selected_path:
        import_from_csv(selected_path)
if __name__ == "__main__":
    main()
