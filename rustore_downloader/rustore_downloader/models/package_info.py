from dataclasses import dataclass
from typing import List, Optional

@dataclass
class DownloadUrl:
    url: str
    size: int
    hash: str

@dataclass
class AppInfo:
    app_id: int
    package_name: str
    app_name: str
    version_name: str
    version_code: int
    file_size: int
    download_urls: List[DownloadUrl]
    icon_url: Optional[str] = None
    whats_new: Optional[str] = None
    description: Optional[str] = None

    def __str__(self):
        return (f"App: {self.app_name} ({self.package_name})\n"
                f"Version: {self.version_name} (code: {self.version_code})\n"
                f"Size: {self.file_size / (1024 * 1024):.2f} MB\n"
                f"Download URLs: {len(self.download_urls)} available")