import requests
import os
from typing import Optional
from rustore_downloader.config.settings import settings
from tqdm import tqdm

def download_file(url: str, destination: str) -> str:
    """Download a file with progress bar"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(destination, 'wb') as file, tqdm(
            desc=os.path.basename(destination),
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as progress_bar:
            for chunk in response.iter_content(chunk_size=settings.DOWNLOAD_CHUNK_SIZE):
                if chunk:
                    file.write(chunk)
                    progress_bar.update(len(chunk))
                    
        return destination
    except requests.RequestException as e:
        if os.path.exists(destination):
            os.remove(destination)
        raise Exception(f"Failed to download file: {str(e)}") from e