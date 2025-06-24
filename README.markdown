# Personalized Learning Assistant

A web-based application powered by a large language model (Mistral-7B) to generate personalized study plans, answer educational questions, and provide visual diagrams.

## Features
- Personalized study plans for subjects like Mathematics, Science, History, and Literature.
- Detailed answers to user questions.
- Diagram generation for visual explanations (using Stable Diffusion API).
- User-friendly web interface built with Streamlit.

## Prerequisites
- Python 3.11
- A Hugging Face account and API token for model access
- A Stable Diffusion API key (optional for diagram generation)
- GPU (recommended for faster LLM inference)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/learning-assistant.git
   cd learning-assistant
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set environment variables:
   - Create a `.env` file:
     ```bash
     echo "HUGGINGFACE_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" > .env
     echo "STABLE_DIFFUSION_API_KEY=your-api-key-here" >> .env
     ```
5. Authenticate with Hugging Face:
   ```bash
   pip install huggingface_hub
   huggingface-cli login
   ```
   - Paste your Hugging Face token when prompted.
6. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the web interface in your browser (default: `http://localhost:8501`).
2. Select a subject and learning level.
3. Enter a question or request a diagram (e.g., "Explain the water cycle with a diagram").
4. Submit to view the study plan, answer, and diagram (if requested).

## Troubleshooting
- **Dependency Conflicts**: Ensure all packages match `requirements.txt`. Reinstall if needed:
  ```bash
  pip uninstall transformers huggingface_hub tokenizers accelerate datasets peft safetensors requests -y
  pip install -r requirements.txt
  ```
- **Gated Model Error**: Request access to Mistral-7B at https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2 and use a valid Hugging Face token.
- **Cache Issues**: Clear the Hugging Face cache if model loading fails:
  ```bash
  rm -rf ~/.cache/huggingface/hub
  ```
- **Diagram Issues**: Verify your Stable Diffusion API key in `.env`.

## Project Structure
- `app.py`: Main Streamlit application.
- `llm_utils.py`: Functions for LLM inference and API interactions.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Notes
- Mistral-7B requires a Hugging Face token. For testing, use `distilgpt2` by updating `MODEL_NAME` in `llm_utils.py`.
- Diagram generation requires a Stable Diffusion API key.
- For faster inference, use a GPU with at least 12GB VRAM.

## Future Improvements
- Fine-tune the LLM on a curated educational dataset.
- Add support for video summarization using YouTube API.
- Implement user authentication and progress tracking.

## License
MIT License