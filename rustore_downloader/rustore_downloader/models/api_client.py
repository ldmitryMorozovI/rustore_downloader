import json
import requests
from typing import Optional, Dict, Any
from urllib.parse import urljoin
from rustore_downloader.config.settings import settings
from rustore_downloader.models.package_info import AppInfo, DownloadUrl

class RuStoreAPIError(Exception):
    """Custom exception for API errors"""
    pass

class RuStoreAPIClient:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.headers = settings.DEFAULT_HEADERS.copy()
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
    def get_app_info(self, package_name: str) -> Optional[AppInfo]:
        """Get application information by package name"""
        url = urljoin(self.base_url, settings.APP_INFO_URL.format(package_name=package_name))
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data.get("code") != "OK":
                return None
                
            body = data.get("body", {})
            return AppInfo(
                app_id=body.get("appId"),
                package_name=body.get("packageName"),
                app_name=body.get("appName"),
                version_name=body.get("versionName"),
                version_code=body.get("versionCode"),
                file_size=body.get("fileSize"),
                icon_url=body.get("iconUrl"),
                whats_new=body.get("whatsNew"),
                description=body.get("shortDescription"),
                download_urls=[]
            )
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            raise RuStoreAPIError(f"Failed to get app info: {str(e)}") from e
    
    def get_download_url(self, app_id: int, version_code: int) -> Optional[AppInfo]:
        """Get download URL for the application"""
        url = urljoin(self.base_url, settings.DOWNLOAD_URL)
        payload = {
            "appId": app_id,
            "firstInstall": True,
            "mobileServices": ["GMS"],
            "supportedAbis": ["arm64-v8a", "armeabi-v7a", "armeabi"],
            "screenDensity": 440,
            "supportedLocales": ["ru_RU"],
            "sdkVersion": 33,
            "withoutSplits": False,
            "signatureFingerprint": None
        }
        
        try:
            headers = self.headers.copy()
            headers["Content-Type"] = "application/json; charset=utf-8"
            
            response = self.session.post(
                url,
                headers=headers,
                data=json.dumps(payload))
            response.raise_for_status()
            
            data = response.json()
            if data.get("code") != "OK":
                return None
                
            body = data.get("body", {})
            download_urls = [
                DownloadUrl(url=item["url"], size=item["size"], hash=item["hash"])
                for item in body.get("downloadUrls", [])
            ]
            
            return AppInfo(
                app_id=body.get("appId"),
                package_name="",  # Not available in this response
                app_name="",      # Not available in this response
                version_name="",  # Not available in this response
                version_code=body.get("versionCode"),
                file_size=0,     # Will be set from download URLs
                download_urls=download_urls
            )
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            raise RuStoreAPIError(f"Failed to get download URL: {str(e)}") from e