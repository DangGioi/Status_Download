import os
import sys
import time

def get_file_size(file_path):
    """Get the size of the file in bytes."""
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        print(f"File {file_path} does not exist.")
        return None

def convert_size(size_in_bytes):
    """Convert size from bytes to a more readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024

def loading_bar(iteration, total, length=50):
    """Display a progress bar in the command line."""
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\rProgress: |{bar}| {percent}% Complete')
    sys.stdout.flush()

def process_file(file_path, download_speed_mbps):
    """Simulate processing or downloading a file with real-time progress."""
    file_size = get_file_size(file_path)
    if file_size is None:
        return

    file_size_mb = file_size / (1024 * 1024)  # Convert file size to MB
    total_steps = int(file_size_mb * 1024 * 1024)  # Number of steps in bytes

    # Simulation setup
    start_time = time.time()
    downloaded_size = 0

    print(f"Downloading file of size: {convert_size(file_size)}")
    
    while downloaded_size < file_size:
        # Simulate downloading chunk
        chunk_size = download_speed_mbps * 1024 * 1024 * (1 / 10)  # Simulate chunk size
        time.sleep(1)  # Simulate time taken to download the chunk

        downloaded_size += chunk_size
        if downloaded_size > file_size:
            downloaded_size = file_size

        elapsed_time = time.time() - start_time
        speed_mbps = (downloaded_size / (1024 * 1024)) / elapsed_time  # Speed in MB/s
        estimated_total_time = (file_size / (1024 * 1024)) / speed_mbps
        remaining_time = estimated_total_time - elapsed_time

        loading_bar(downloaded_size, file_size)
        print(f" - Speed: {speed_mbps:.2f} MB/s | Remaining time: {remaining_time:.2f} seconds", end='')

    print("\nDownload Complete!")

# Example usage
file_path = r"C:\Users\ADMIN\Downloads\Anaconda3-2018.12-Windows-x86_64.exe"  # Path to your file
download_speed_mbps = 10  # Simulate download speed of 10 MB/s
process_file(file_path, download_speed_mbps)
