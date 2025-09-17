import pathlib
import subprocess
import shutil

def reencode_music_viv(output_viv_name="zzzymus.viv"):
    source_dir = pathlib.Path("input")
    dest_dir = pathlib.Path(".")

    for f in dest_dir.iterdir():
        if f.is_file() and not f.suffix:
            f.unlink()

    originals = [f for f in source_dir.iterdir() if f.is_file() and not f.suffix]

    converted = [f for f in source_dir.iterdir() if f.is_file() and f.suffix.lower() == ".asf"]

    all_files = sorted(set(f.name for f in originals) |
                       set(f.stem for f in converted))

    print(converted)
    for name in all_files:
        converted_file = source_dir / f"{name}.asf"
        original_file = source_dir / name
        target_path = dest_dir / name

        if converted_file.exists():
            print(f"Importing converted file : {converted_file.name}")
            shutil.copyfile(converted_file, target_path)
        elif original_file.exists():
            print(f"Importing original file : {original_file.name}")
            shutil.copyfile(original_file, target_path)

    final_files = sorted(dest_dir.iterdir())
    final_paths = [str(f) for f in final_files if f.is_file() and not f.suffix]

    #print("List of files imported in : ", output_viv_name, ":", final_paths)

    command = ["vivenc", output_viv_name] + final_paths
    subprocess.run(command, check=True)

    print(f"{output_viv_name} built with success.")

if __name__ == "__main__":
    reencode_music_viv()