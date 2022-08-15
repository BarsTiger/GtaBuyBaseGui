# GtaBuyBase GUI

GUIfyed end extended version of best GTA Online wishlist app

Features:

- Filters system
- Multiple databases
- Owning items and profiles 
- Modern design themes
- Images for items (you can use gtabase.com, for example, to get images)
- Error protection

To run app with logs, use:

```
GtaBuyBaseGui.exe | more
```

Custom build:

```
python -m venv venv
pip install -r requirements.txt
pyinstaller --onefile --windowed --icon gui/img/icon.ico GtaBuyBaseGui.py
```

