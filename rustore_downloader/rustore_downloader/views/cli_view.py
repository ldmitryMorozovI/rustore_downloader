import argparse
from typing import Optional
from rustore_downloader.models.package_info import AppInfo
from rustore_downloader.controllers.download_controller import DownloadController, DownloadControllerError
from rustore_downloader.utils.logger import logger

class CLIView:
    def __init__(self):
        self.controller = DownloadController()
        
    def parse_args(self):
        """Parse command line arguments"""
        parser = argparse.ArgumentParser(
            description="RuStore APK Downloader - Download APK files from RuStore")
        
        parser.add_argument(
            "package_name",
            help="Package name to download (e.g., ru.sberbankmobile)")
        
        parser.add_argument(
            "-d", "--download-dir",
            help="Directory to save downloaded APK",
            default=None)
            
        parser.add_argument(
            "-v", "--verbose",
            action="store_true",
            help="Enable verbose output")
            
        return parser.parse_args()
    
    def display_app_info(self, app_info: AppInfo):
        """Display application information"""
        print("\nApplication Information:")
        print("=" * 40)
        print(f"Name: {app_info.app_name}")
        print(f"Package: {app_info.package_name}")
        print(f"Version: {app_info.version_name} (code: {app_info.version_code})")
        print(f"Size: {app_info.file_size / (1024 * 1024):.2f} MB")
        print(f"Description: {app_info.description or 'N/A'}")
        print("\nDownload URLs:")
        for idx, url in enumerate(app_info.download_urls, 1):
            print(f"{idx}. {url.url}")
        print("=" * 40 + "\n")
    
    def run(self):
        """Run the CLI application"""
        args = self.parse_args()
        
        try:
            # Get package information
            logger.info(f"Fetching info for package: {args.package_name}")
            app_info = self.controller.get_package_info(args.package_name)
            
            if not app_info:
                print(f"Error: Package '{args.package_name}' not found or inaccessible")
                return
                
            self.display_app_info(app_info)
            
            # Download the package
            logger.info("Starting download...")
            print(f"Downloading {app_info.app_name}...")
            downloaded_path = self.controller.download_package(app_info, args.download_dir)
            
            print(f"\nSuccessfully downloaded to: {downloaded_path}")
            logger.info(f"Download completed: {downloaded_path}")
            
        except DownloadControllerError as e:
            print(f"Error: {str(e)}")
            logger.error(str(e))
        except KeyboardInterrupt:
            print("\nDownload cancelled by user")
            logger.warning("Download cancelled by user")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            logger.exception("Unexpected error occurred")