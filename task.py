import os
import time
import pdfkit
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Folder path to monitor. here we have named it as 'test'.
FOLDER_TO_WATCH = "test"

# Cache to store file modification times
file_mod_times = {}


# custom function to convert HTML to PDF
def convert_html_to_pdf(html_file_path):
    pdf_file_path = html_file_path.replace(".html", ".pdf")
    try:
        options = {
            'enable-local-file-access': None # allowing all the local resources to be accessed
        }
        pdfkit.from_file(html_file_path, pdf_file_path, options=options)
        print(f"Converted: {html_file_path} -> {pdf_file_path}")
    except Exception as e:
        print(f"Failed to convert {html_file_path} to PDF: {e}")


# custom function to check if a file has been modified
def has_file_been_modified(file_path):
    # Get the last modification time
    mod_time = os.path.getmtime(file_path)
    # If file is new or modified, return True
    if file_path not in file_mod_times or file_mod_times[file_path] != mod_time:
        file_mod_times[file_path] = mod_time
        return True
    return False


# class for watchdog
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # If an HTML file is modified, convert it to PDF
        if event.src_path.endswith(".html") and has_file_been_modified(event.src_path):
            convert_html_to_pdf(event.src_path)

    def on_created(self, event):
        # If a new HTML file is created, convert it to PDF
        if event.src_path.endswith(".html"):
            convert_html_to_pdf(event.src_path)


# Monitoring the folder 'test'
def monitor_folder():
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_WATCH, recursive=False)
    observer.start()
    print(f"Monitoring folder: {FOLDER_TO_WATCH}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    # Initial conversion of all HTML files in the folder
    for file in os.listdir(FOLDER_TO_WATCH):
        if file.endswith(".html"):
            file_path = os.path.join(FOLDER_TO_WATCH, file)
            if has_file_been_modified(file_path):
                convert_html_to_pdf(file_path)

    # Starting the monitoring of the folder
    monitor_folder()
