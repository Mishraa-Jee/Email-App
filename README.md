# 📧 Job Email Generator

An AI-powered Streamlit application that automatically generates personalized job application emails by analyzing job postings and matching them with your portfolio skills.

## ✨ Features

- **Web Scraping**: Extracts job information from career/job posting URLs
- **AI-Powered Analysis**: Uses Groq's Llama model to extract job details (role, experience, skills, description)
- **Portfolio Matching**: Automatically matches job requirements with your portfolio skills using ChromaDB vector search
- **Email Generation**: Creates professional, personalized job application emails
- **User-Friendly Interface**: Clean Streamlit UI with easy-to-use workflow

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mishraa-Jee/Email-App.git
   cd Email-App
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - Get your API key from [Groq Console](https://console.groq.com/)

5. **Update your portfolio**
   - Edit `resource/my_portfolio.csv` with your skills and portfolio links
   - Format: `Technology,Links`
   - Example:
     ```csv
     Technology,Links
     "React, Node.js, MongoDB",https://www.linkedin.com/in/your-profile/
     "Python, Django, MySQL",https://github.com/your-username/
     ```

6. **Run the application**
   ```bash
   streamlit run main.py
   ```

7. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

## ☁️ Deploy to Streamlit Community Cloud

Streamlit Community Cloud provides free hosting for Streamlit apps. Follow these steps:

### Prerequisites

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Streamlit Cloud deployment"
   git push origin main
   ```

2. **Ensure your repository is public** (required for free tier)

### Deployment Steps

1. **Sign up/Login to Streamlit Community Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

2. **Deploy your app**
   - Click "New app"
   - Select your repository: `Mishraa-Jee/Email-App`
   - Select branch: `main`
   - Main file path: `main.py`
   - Click "Deploy"

3. **Configure Secrets**
   - In your app settings, go to "Secrets"
   - Add your Groq API key:
     ```toml
     GROQ_API_KEY = "your_groq_api_key_here"
     ```
   - Click "Save"

4. **Wait for deployment**
   - Streamlit will install dependencies from `requirements.txt`
   - The app will be available at `https://your-app-name.streamlit.app`

### Important Notes for Cloud Deployment

- ✅ **File paths**: Already fixed to use relative paths (`resource/my_portfolio.csv`)
- ✅ **Environment variables**: Use Streamlit's Secrets management (not `.env` file)
- ✅ **Vectorstore**: ChromaDB will create a new vectorstore on each deployment (this is fine for this use case)
- ✅ **Dependencies**: All required packages are listed in `requirements.txt`

### Troubleshooting

**Issue**: App fails to start
- Check that `requirements.txt` includes all dependencies
- Verify your Groq API key is set correctly in Secrets
- Check the logs in Streamlit Cloud dashboard

**Issue**: Portfolio file not found
- Ensure `resource/my_portfolio.csv` exists in your repository
- Verify the file path in `portfolio.py` is correct (`resource/my_portfolio.csv`)

**Issue**: Vectorstore errors
- ChromaDB will recreate the vectorstore automatically on first run
- This is normal behavior in cloud deployments

## 📁 Project Structure

```
Email-App/
├── main.py                 # Streamlit app entry point
├── chains.py               # LangChain LLM chains for job extraction and email generation
├── portfolio.py            # Portfolio management with ChromaDB vector search
├── utils.py                # Text cleaning utilities
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── .env                   # Environment variables (local only, not committed)
├── resource/
│   └── my_portfolio.csv   # Your portfolio skills and links
└── vectorstore/          # ChromaDB persistent storage (auto-generated, gitignored)
```

## 🔧 Configuration

### Customizing the Email Template

Edit the prompt in `chains.py`, specifically the `write_mail` method:

```python
prompt_email = PromptTemplate.from_template(
    """
    ### JOB DESCRIPTION:
    {job_description}

    ### INSTRUCTION:         
    I am [Your Name], [Your Title] at [Your Institution] currently seeking for job. 
    ...
    """
)
```

### Updating Portfolio Skills

Edit `resource/my_portfolio.csv` to add or modify your skills and portfolio links.

## 🔐 Security

- **Never commit `.env` file** - It's already in `.gitignore`
- **Use Streamlit Secrets** for cloud deployment
- **Keep your API keys secure** - Don't share them publicly

## 🛠️ Technologies Used

- **Streamlit** - Web application framework
- **LangChain** - LLM orchestration
- **Groq** - Fast LLM inference (Llama 3.1 8B)
- **ChromaDB** - Vector database for portfolio matching
- **BeautifulSoup4** - Web scraping
- **Pandas** - Data manipulation

## 📝 License

This project is open source and available for personal use.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or issues, please open an issue on GitHub.

---

**Note**: Make sure to replace placeholder information (like your name, LinkedIn profile, etc.) in `chains.py` and `resource/my_portfolio.csv` with your actual details before deploying.

