# AI Resume Critiquer

An intelligent resume analysis tool powered by Groq's LLaMA AI models. Upload your resume and get personalized feedback to improve your chances of landing your dream job!

## Features

- **PDF & TXT Support**: Upload resumes in PDF or plain text format
- **AI-Powered Analysis**: Leverages Groq's fast LLaMA 3 models for detailed feedback
- **Job-Role Specific**: Tailor feedback based on your target job position
- **Structured Feedback**: Get analysis on content clarity, skills presentation, and experience descriptions
- **User-Friendly Interface**: Built with Streamlit for an intuitive web-based experience

## Prerequisites

- Python 3.8 or higher
- A Groq API key (get one at https://console.groq.com)
- Streamlit

## Installation

1. Clone or download this project
2. Navigate to the project directory
3. Install the required dependencies:

```bash
pip install streamlit PyPDF2 langchain-groq groq python-dotenv langchain langchain-community
```

Or using `uv`:

```bash
uv add streamlit PyPDF2 langchain-groq groq python-dotenv langchain langchain-community
```

## Setup

1. Create a `.env` file in the project root directory:

```
GROQ_API_KEY=your_actual_api_key_here
```

2. Replace `your_actual_api_key_here` with your actual Groq API key from https://console.groq.com

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Or with `uv`:

```bash
uv run streamlit run app.py
```

The app will open in your default browser. Then:

1. Click "Browse files" to upload your resume (PDF or TXT)
2. (Optional) Enter the job role you're targeting for more specific feedback
3. Click "Analyze Resume" to get AI-powered feedback
4. Review the structured analysis with recommendations

## How It Works

1. **File Processing**: Extracts text from uploaded PDF or TXT files
2. **AI Analysis**: Sends the resume content to Groq's API with a detailed prompt
3. **Feedback Generation**: Receives structured feedback focusing on:
   - Content clarity and impact
   - Skills presentation
   - Experience descriptions
   - Role-specific improvements

## Configuration

You can modify the following in `app.py`:

- **Model**: Change `model="llama-3.1-8b-instant"` to use different Groq models (check available models at https://console.groq.com)
- **Temperature**: Adjust `temperature=0.7` for response creativity (0 = deterministic, 1 = creative)
- **System Prompt**: Customize the AI reviewer's personality by editing the system message

## Project Structure

- `app.py` - Main Streamlit application
- `.env` - Environment variables (create this file with your API key)
- `README.md` - This file

## Dependencies

- **streamlit** - Web app framework
- **PyPDF2** - PDF file parsing
- **groq** - Groq API client
- **langchain-groq** - LangChain integration for Groq
- **python-dotenv** - Environment variable management
- **langchain** - LLM framework
- **langchain-community** - Community integrations

## Troubleshooting

**"GROQ_API_KEY not found"**
- Check that your `.env` file exists in the project root
- Verify the key format is correct
- Restart the Streamlit app after creating/updating `.env`

**"File does not have any content"**
- Ensure your PDF or TXT file isn't empty
- Try converting PDFs to text manually to verify they contain readable text
- Some encrypted PDFs may not extract text properly

**"ModuleNotFoundError"**
- Make sure all dependencies are installed: `uv add streamlit PyPDF2 langchain-groq groq python-dotenv`
- If using virtual environment, ensure it's activated

**Streamlit not opening in browser**
- The app should automatically open at `http://localhost:8501`
- If it doesn't, manually navigate to that URL in your browser

## Future Enhancements

Possible improvements:
- Support for DOCX format
- Resume comparison with job descriptions
- Export analysis as PDF
- Multiple resume uploads for comparison
- Resume scoring system
- Personalized templates and suggestions

## Tips for Best Results

- Use a well-formatted resume (clear sections, proper spacing)
- Be specific about your target job role for tailored feedback
- Upload a recent version of your resume
- PDFs work best when they're text-based (not scanned images)

## License

This is a simple project for learning purposes.
