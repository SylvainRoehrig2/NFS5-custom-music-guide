import pathlib
import subprocess

source_dir = pathlib.Path("to_be_converted")
dest_dir = pathlib.Path("converted")

def convert_to_compatible_wav(input_file: pathlib.Path, output_file: pathlib.Path):
    command = [
        "ffmpeg", "-y", "-i", str(input_file),
        "-ar", "32000", "-ac", "2", "-sample_fmt", "s16",
        str(output_file)
    ]
    subprocess.run(command, check=True)

def convert_all_audio():
    supported_inputs = [".mp3", ".opus", ".flac", ".ogg", ".m4a", ".aac", ".wav"]

    # S'assurer que le dossier destination existe
    dest_dir.mkdir(parents=True, exist_ok=True)

    input_files = [
        f for f in source_dir.iterdir()
        if f.is_file() and f.suffix.lower() in supported_inputs
    ]

    if not input_files:
        print(f"No audio file to be converted found. Put them in a folder named '{source_dir}'.")
        return

    for f in input_files:
        output_file = dest_dir / (f.stem + ".wav")
        print(f"Conversion : {f.name} → {output_file.name} (32kHz PCM)")
        convert_to_compatible_wav(f, output_file)

    print(f"All converted files are in the folder '{dest_dir}'.")

if __name__ == "__main__":
    convert_all_audio()
