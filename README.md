# Vimeo Downloader

A console-based tool to download videos from Vimeo.

## Description

This Python script allows you to download videos from Vimeo using the command line. It uses the `vimeo_downloader` library to fetch and download video content.

## Features

- Download videos from Vimeo URLs
- Command-line interface
- Automatic selection of best quality stream
- Simple and easy to use

## Requirements

- Python 3
- `vimeo_downloader` library

## Installation

1. Install the vimeo_downloader library:
```bash
pip install git+https://github.com/yashrathi-git/vimeo_downloader
```

2. Clone this repository or download the script.

## Usage

### Basic usage

```bash
python vimeo_dl.py https://vimeo.com/91852770
```

Or with the player URL format:

```bash
python vimeo_dl.py https://player.vimeo.com/video/91852770
```

### List videos

```bash
python vimeo_list.py <vimeo_url>
```

## Configuration

You may need to configure cookies in `vimeo_dl.py` for private or restricted videos. Edit the `cookies` variable in the script if needed.

## Notes

- The script automatically selects the best quality stream available
- Downloaded videos are saved in the current directory
- Make sure you have the necessary permissions to download the video

## Credits

This project uses the [vimeo_downloader](https://github.com/yashrathi-git/vimeo_downloader) library by yashrathi-git.

## Author

Fernando Ortega Gorrita (@fernandoog)

## License

See LICENSE file for details.
