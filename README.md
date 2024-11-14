# HTML TO PDF CONVERSION

This project monitors a test folder for any new or modified `.html` files and automatically converts them to `.pdf` format. The conversion is handled only when a change is detected, optimizing resources and processing time.

## Features

- Monitors a folder for any new or modified `.html` files.
- Converts the updated `.html` file to `.pdf` format.
- Uses `pdfkit` for HTML to PDF conversion, leveraging `wkhtmltopdf`.
- Efficient monitoring with the `watchdog` library to track file system events.
- Initial conversion of all `.html` files in the folder at startup.

## Requirements

Before running this project, ensure you have the following:

- Python 3.x
- **`pdfkit`** library (used for HTML to PDF conversion)
- **`watchdog`** library (used for file monitoring)
- **`wkhtmltopdf`** tool (required by `pdfkit` for converting HTML to PDF)

### Step 1: Set the Folder to Monitor
Modify the `FOLDER_TO_WATCH` variable in the code to specify the folder you want to monitor. In this repo, the 'test' folder is monitored.

```python
FOLDER_TO_WATCH = "path/to/your/folder"
```

### Step 2: Run the Script
Run the script to start monitoring the folder and automatically convert any `.html` files to `.pdf`.

```bash
python task.py
```

### Step 3: Monitoring & Conversion
- When a new `.html` file is added to the folder, it will be automatically converted to `.pdf`.
- If an existing `.html` file is modified, only the modified file will be converted to `.pdf`.
- The `.pdf` file will be saved with the same name as the `.html` file but with a `.pdf` extension.

### Step 4: Initial Conversion
At the start of the program, all existing `.html` files in the specified folder will be checked and converted to `.pdf` if they haven't already been converted or modified.

## File Structure

```
project_folder/
│
├── task.py    # Python script for monitoring and conversion
├── test/                 # Folder to watch for HTML files
│   ├── a.html            # Sample HTML file
│   ├── b.html            # Another HTML file
│   └── ...
└── README.md                 # Project documentation (this file)
```

## How It Works

1. The script monitors the specified folder for file events (like file creation or modification) using the `watchdog` library.
2. When a new `.html` file is created or an existing `.html` file is modified, the `convert_html_to_pdf` function is triggered.
3. The `pdfkit.from_file()` method is used to convert the `.html` file to a `.pdf` file, with `wkhtmltopdf` being the underlying engine for conversion.
4. The system ensures that only modified or newly created `.html` files are processed, optimizing for performance.
