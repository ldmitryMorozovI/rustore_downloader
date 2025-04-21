from rustore_downloader.views.cli_view import CLIView

def main():
    """Entry point for the application"""
    cli = CLIView()
    cli.run()

if __name__ == "__main__":
    main()