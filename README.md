# ObsidiAnki GPT Assistant

ObsidiAnki GPT Assistant is a Python-based application designed to leverage the OpenAI API for generating concise, informative notes on a wide range of topics. These notes are automatically saved in Markdown format, making them ideal for quick reference, study materials, or content creation. The application utilizes rich logging for enhanced visual feedback during operation.

## Features

- **OpenAI API Integration**: Utilize the advanced capabilities of OpenAI's models to generate notes.
- **Rich Logging**: Get real-time, colorful logs for better tracking of the application's processes.
- **Markdown Format**: Notes are saved in Markdown format for easy readability and compatibility with various platforms.
- **Customizable**: Through environment variables, easily customize API keys and other settings.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or newer
- An active OpenAI API subscription
- The following Python packages: `python-dotenv`, `rich`, `requests`, `openai`

## Installation

To install ObsidiAnki GPT Assistant, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory and install the required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and populate it with your `OPENAI_API_KEY`:

```plaintext
OPENAI_API_KEY=your_api_key_here
```

## Usage

To use ObsidiAnki GPT Assistant, run the main script from the terminal:

```bash
python main.py
```

Follow the prompt to enter the topic you wish to generate a note for. The application will communicate with the OpenAI API to create a note, which will then be saved in the `notes` directory as a Markdown file.

## Configuration

- **API Key**: Set your OpenAI API key in the `.env` file.
- **Logging Level**: Adjust the logging level in `config/cfg.py` if needed.

## Contributing

We welcome contributions to ObsidiAnki GPT Assistant. Please open an issue or submit a pull request with your proposed changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.