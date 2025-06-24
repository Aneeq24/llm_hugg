# Personalized Learning Assistant

A web-based application powered by a large language model (Mistral-7B) to generate personalized study plans, answer educational questions, and provide visual diagrams.

## Features
- Personalized study plans for subjects like Mathematics, Science, History, and Literature.
- Detailed answers to user questions.
- Diagram generation for visual explanations (using Stable Diffusion API).
- User-friendly web interface built with Streamlit.

## Prerequisites
- Python 3.9 or higher
- A Hugging Face account for model access
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
4. Set environment variables (optional):
   - Create a `.env` file and add your Stable Diffusion API key:
     ```bash
     STABLE_DIFFUSION_API_KEY=your-api-key-here
     ```
5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the web interface in your browser (default: `http://localhost:8501`).
2. Select a subject and learning level.
3. Enter a question or request a diagram (e.g., "Explain the water cycle with a diagram").
4. Submit to view the study plan, answer, and diagram (if requested).

## Project Structure
- `app.py`: Main Streamlit application.
- `llm_utils.py`: Functions for LLM inference and API interactions.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Notes
- The project uses Mistral-7B for text generation. For production, consider fine-tuning the model on a custom educational dataset.
- Diagram generation requires a Stable Diffusion API key. Without it, diagrams will not be generated.
- For faster inference, use a GPU with at least 12GB VRAM.

## Future Improvements
- Fine-tune the LLM on a curated educational dataset.
- Add support for video summarization using YouTube API.
- Implement user authentication and progress tracking.

## License
MIT License