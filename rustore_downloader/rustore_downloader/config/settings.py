import os
from pathlib import Path

class Settings:
    # Default user agent to mimic RuStore app
    USER_AGENT = "RuStore/1.66.0.3 (Android 13; SDK 33; arm64-v8a, armeabi-v7a, armeabi; Xiaomi Mi 9T; ru)"
    
    # Default headers for API requests
    DEFAULT_HEADERS = {
        "Accept-Encoding": "gzip",
        "androidSdkVer": "33",
        "Connection": "Keep-Alive",
        "deviceId": "44cbcaad40cfabe7-1552871320",
        "deviceManufacturerName": "Xiaomi",
        "deviceModel": "Xiaomi Mi 9T",
        "deviceModelName": "Mi 9T",
        "deviceType": "mobile",
        "firmwareLang": "ru",
        "firmwareVer": "13",
        "User-Agent": USER_AGENT,
        "ruStoreVerCode": "1066003",
    }
    
    # API endpoints
    BASE_URL = "https://backapi.rustore.ru"
    APP_INFO_URL = "/applicationData/overallInfo/{package_name}"
    DOWNLOAD_URL = "/applicationData/v2/download-link"
    
    # Download settings
    DOWNLOAD_CHUNK_SIZE = 8192
    DEFAULT_DOWNLOAD_DIR = str(Path.cwd() / "rustore_downloads")
    
    # Logging settings
    LOG_DIR = str(Path.cwd() / ".rustore_downloader" / "logs")
    LOG_FILE = "rustore_downloader.log"
    LOG_LEVEL = "INFO"
    
    @classmethod
    def ensure_directories_exist(cls):
        """Ensure required directories exist"""
        os.makedirs(cls.DEFAULT_DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(cls.LOG_DIR, exist_ok=True)

settings = Settings()