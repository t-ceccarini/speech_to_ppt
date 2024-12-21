
# Speech to PPT

## Overview
**Speech to PPT** is a Python-based project designed to streamline the process of converting speech into a structured PowerPoint presentation. It provides functionalities to transcribe audio files, generate slides with relevant content, and add explanations to enhance the presentation.

### Features
- **Transcription**: Converts speech from audio files into text.
- **Presentation Creation**: Automatically generates PowerPoint slides from the transcribed text.
- **Explanations**: Enriches the slides with additional explanations or context.
- **Pipeline Integration**: Combines the entire workflow into an automated process.

## Installation

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd speech_to_ppt
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Prepare an audio file for transcription and place it in the `data/raw` directory.
2. Run the pipeline script to process the audio and generate the presentation:
   ```bash
   python -m speech_to_ppt.pipeline
   ```
3. Find the generated PowerPoint presentation in the `data/presentations` directory.

## Project Structure
- **`speech_to_ppt/`**: Core Python modules for transcription, explanation, and presentation.
- **`data/`**: Contains raw audio files, intermediate outputs, and final presentations.
- **`docs/`**: Documentation for the project.
- **`requirements.txt`**: Lists required Python packages.

## License
This project is licensed under the terms of the `LICENSE` file included in the repository.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or new features.
