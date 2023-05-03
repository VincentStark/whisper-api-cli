# OpenAI Whisper API Python CLI

This repository contains two Python CLI scripts to interact with OpenAI's Whisper API for transcribing and translating audio files.

## Requirements

- Python 3.6 or higher
- `python-dotenv` library
- `requests` library

## Installation

- Clone this repository:

```bash
git clone https://github.com/VincentStark/whisper-api-cli.git
cd openai-audio-api-cli
```

- Install the required libraries:

```shell
pip install -r requirements.txt
```

- Create a `.env` file in the project directory with the following content:

```shell
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

## Usage

### Transcribe Audio

To transcribe an audio file, use the `transcribe.py` script:

```shell
python transcribe.py [--language LANGUAGE_CODE] /path/to/audio/file
```

Example:

```shell
python transcribe.py --language en /path/to/file/audio.mp3
```

### Translate Audio

To translate an audio file, use the `translate.py` script:

```shell
python translate.py /path/to/audio/file
```

Example:

```shell
python translate.py /path/to/file/german.m4a
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
