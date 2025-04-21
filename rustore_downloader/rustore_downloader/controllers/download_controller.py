from typing import Optional
from rustore_downloader.models.api_client import RuStoreAPIClient, RuStoreAPIError
from rustore_downloader.models.package_info import AppInfo
from rustore_downloader.utils.file_utils import download_file
from rustore_downloader.config.settings import settings
import os

class DownloadController:
    def __init__(self):
        self.api_client = RuStoreAPIClient()
        
    def get_package_info(self, package_name: str) -> Optional[AppInfo]:
        """Get package information including download URLs"""
        try:
            # First get basic app info
            app_info = self.api_client.get_app_info(package_name)
            if not app_info:
                return None
                
            # Then get download URLs
            download_info = self.api_client.get_download_url(app_info.app_id, app_info.version_code)
            if not download_info:
                return None
                
            # Merge the information
            app_info.download_urls = download_info.download_urls
            return app_info
        except RuStoreAPIError as e:
            raise DownloadControllerError(str(e)) from e
    
    def download_package(self, app_info: AppInfo, download_dir: str = None) -> str:
        """Download the package to specified directory"""
        if not app_info.download_urls:
            raise DownloadControllerError("No download URLs available")
            
        download_dir = download_dir or settings.DEFAULT_DOWNLOAD_DIR
        os.makedirs(download_dir, exist_ok=True)
        
        # Use the first download URL
        download_url = app_info.download_urls[0]
        file_name = f"{app_info.package_name}_{app_info.version_code}.zip"
        file_path = os.path.join(download_dir, file_name)
        
        try:
            return download_file(download_url.url, file_path)
        except Exception as e:
            raise DownloadControllerError(f"Download failed: {str(e)}") from e

class DownloadControllerError(Exception):
    """Custom exception for controller errors"""
    pass