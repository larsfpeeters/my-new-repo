# Python Hello World Server

A simple Flask web server that returns "Hello, World!" on localhost.

## Features

- Simple HTTP server running on localhost:5000
- Hello World endpoint at `/`
- Health check endpoint at `/health`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/larsfpeeters/my-new-repo.git
   cd my-new-repo
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the server:
   ```bash
   python app.py
   ```

2. Open your browser and visit:
   - `http://127.0.0.1:5000/` - Hello World message
   - `http://127.0.0.1:5000/health` - Health check

## Development

The server runs in debug mode by default, so changes to the code will automatically reload the server.