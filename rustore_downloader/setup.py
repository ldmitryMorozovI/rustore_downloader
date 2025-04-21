from setuptools import setup, find_packages

setup(
    name="rustore_downloader",
    version="1.0.0",
    description="RuStore APK Downloader - Download APK files from RuStore",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "tqdm>=4.66.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "rustore-downloader=rustore_downloader.main:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)