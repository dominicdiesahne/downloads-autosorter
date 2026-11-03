# Downloads Auto-Sorter
 
A small Python script that tidies up your Downloads folder by moving files into subfolders based on their file type.
 
Before:
 
```
Downloads/
├── holiday.jpg
├── invoice_march.pdf
├── setup.exe
├── project.zip
└── song.mp3
```
 
After:
 
```
Downloads/
├── Images/holiday.jpg
├── Documents/invoice_march.pdf
├── Installers/setup.exe
├── Archives/project.zip
└── Audio/song.mp3
```
 
## Features
 
- Sorts files into **Images**, **Documents**, **Archives**, **Installers**, **Audio** and **Video**
- Creates category folders automatically when they're needed
- Leaves existing folders and unrecognized file types untouched
- Uses only the Python standard library — no installs required
- Works on Windows, macOS and Linux
## Requirements
 
- Python 3.8 or newer
## Installation
 
Clone the repository or download the script:
 
```bash
git clone https://github.com/<your-username>/downloads-auto-sorter.git
cd downloads-auto-sorter
```
 
## Usage
 
Run the script once to sort everything currently in your Downloads folder:
 
```bash
python sorter.py
```
 
Each move is printed to the console:
 
```
Moved holiday.jpg -> Images
Moved invoice_march.pdf -> Documents
```
 
## Configuration
 
Categories and extensions are defined in the `CATEGORIES` dictionary at the top of `sorter.py`. Add, remove or rename categories as you like:
 
```python
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Code": [".py", ".js", ".html", ".css"],   # new category
}
```
 
To sort a different folder, change `DOWNLOADS`:
 
```python
DOWNLOADS = Path.home() / "Desktop"
```
 
Extension matching is case-insensitive, so `.JPG` and `.jpg` are treated the same.
 
## Running it automatically
 
**Windows (Task Scheduler)**
 
1. Open Task Scheduler and choose **Create Basic Task**.
2. Pick a trigger, such as daily or at log on.
3. For the action, choose **Start a program**, set the program to `python` and the argument to the full path of `sorter.py`.
**macOS / Linux (cron)**
 
Run `crontab -e` and add a line like this to sort every hour:
 
```
0 * * * * /usr/bin/python3 /path/to/sorter.py
```
 
## Known limitations
 
- If a file with the same name already exists in the target folder, the move will fail or overwrite it, depending on your operating system. Collision handling is on the roadmap.
- Files that are still downloading (e.g. `.crdownload`, `.part`) are skipped only because their extensions aren't listed — keep it that way.
- Sorting runs once per execution; it doesn't watch the folder in real time yet.
## Roadmap
 
- [ ] Rename duplicates instead of overwriting (`file (1).pdf`)
- [ ] Real-time sorting with [`watchdog`](https://pypi.org/project/watchdog/)
- [ ] Archive or delete files older than N days
- [ ] Dry-run mode (`--dry-run`) to preview moves
- [ ] Load categories from a `config.json` file
- [ ] Log moves to a file
## Contributing
 
Issues and pull requests are welcome. For bigger changes, open an issue first to discuss what you'd like to change.
 
## License
 
MIT
 