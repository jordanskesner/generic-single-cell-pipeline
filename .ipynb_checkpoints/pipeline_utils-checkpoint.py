#=== Function to download genome sequences and annotations ===#
def download_genome(url, output_dir):
    try:
        print(f"Downloading from {url}")
        urllib.request.urlretrieve(url, output_path)
        print(f"Saved to {output_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")