from pathlib import Path
import shutil

DOWNLOADS = Path.home() / "Downloads"
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Installers": [".exe", ".msi", ".dmg", ".pkg"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Video": [".mp4", ".mkv", ".mov"],
}

def sort_downloads():
    for file in DOWNLOADS.iterdir():
        if not file.is_file():
            continue
        for folder, exts in CATEGORIES.items():
            if file.suffix.lower() in exts:
                target = DOWNLOADS / folder
                target.mkdir(exist_ok=True)
                shutil.move(str(file), target / file.name)
                print(f"Moved {file.name} -> {folder}")
                break

if __name__ == "__main__":
    sort_downloads()