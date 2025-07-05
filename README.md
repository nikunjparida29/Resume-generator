# AI-Powered Resume Generator

This project provides a user-friendly web application built with Streamlit that leverages Google's Generative AI (Gemini Pro) to help you quickly draft professional resume sections. Simply provide your raw information for the summary, experience, education, and skills, and the AI will expand and format it into compelling resume content.

## Features

* **AI-Powered Content Generation:** Uses Google Gemini Pro to craft impactful summaries, detailed experience bullet points, formatted education entries, and categorized skill lists.
* **Interactive Web UI:** Built with Streamlit for an intuitive and easy-to-use interface.
* **Dynamic Experience Fields:** Add or remove multiple job experience input fields as needed.
* **Copy & Download Options:** Easily copy the generated resume content to your clipboard or download it as a Markdown (.md) file.
* **Secure API Key Handling:** Utilizes .env files for safely storing your Google API Key, keeping it out of your code.

## Getting Started

Follow these steps to set up and run the application on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+**: Download from [python.org](https://www.python.org/downloads/).
* **Google Generative AI API Key**:
    * Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
    * Log in with your Google account.
    * Click "Get API Key" or "Create API Key".
    * **Keep this key safe!** You will need it in the next steps.

### Installation & Setup

1.  **Navigate to the Project Directory:**
    Open your terminal or VS Code's integrated terminal and navigate to your project folder:
    ```bash
    cd C:\Users\USER\OneDrive\Desktop\ibm project python\
    ```
    (Replace the path with your actual project directory).

2.  **Create a Python Virtual Environment:**
    It's highly recommended to use a virtual environment to manage dependencies for your project, keeping them separate from your global Python installation.
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\activate
        ```
        * **Troubleshooting `.\venv\Scripts\activate : File ... cannot be loaded` on Windows:**
            If you get an error about running scripts being disabled, you need to change your PowerShell Execution Policy.
            1.  Close your current terminal.
            2.  Open **Windows PowerShell as Administrator** (Right-click on Start menu, search "PowerShell", then "Run as administrator").
            3.  Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
            4.  Type `Y` and press Enter when prompted.
            5.  Close the Administrator PowerShell and return to your VS Code terminal, then try activating again.
    * **macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **Verify Activation:** Your terminal prompt should now start with `(venv)` (e.g., `(venv) PS C:\Users\USER\OneDrive\Desktop\ibm project python>`).

4.  **Create a `.env` file:**
    * In your project's root directory (the same folder as `resume_generator.py`), create a new file named `.env` (make sure it starts with a dot and has no other name).
    * Open this `.env` file with a text editor (like VS Code).
    * Add your Google API Key to this file in the following format, replacing `YOUR_GEMINI_API_KEY_HERE` with the actual key you obtained:
        ```
        GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"
        ```
    * **Save the `.env` file.**

5.  **Create `requirements.txt` file:**
    * In your project's root directory, create a new file named `requirements.txt`.
    * Paste the following content into it:
        ```
        google-generativeai
        python-dotenv
        streamlit
        pyperclip
        ```
    * **Save the `requirements.txt` file.**

6.  **Install Required Libraries:**
    With your virtual environment active (`(venv)` showing in your terminal prompt), run:
    ```bash
    pip install -r requirements.txt
    ```
    This will install all necessary Python packages.

## Usage

Once all prerequisites are met and dependencies are installed:

1.  **Run the Streamlit Application:**
    Ensure your virtual environment is active (`(venv)` in your terminal prompt).
    ```bash
    streamlit run resume_generator.py
    ```
2.  **Access the App:**
    Your default web browser should automatically open to the Streamlit application (usually `http://localhost:8501`).
3.  **Generate Resume Content:**
    * Fill in the text areas with your professional summary details, job experiences, education, and skills.
    * Use the "Add Another Job" and "Remove Last Job" buttons for dynamic experience entries.
    * Click the "Generate Resume" button.
4.  **Review and Utilize:**
    The generated content will appear below the input form. You can copy it to your clipboard or download it as a Markdown file.

## Configuration

* **Google Gemini Model:** The application is configured to use `gemini-pro` by default. If you encounter `NotFound: 404` errors related to the model (which can happen due to regional availability), you might need to try a different model.
    * **How to find available models:**
        Open your `test_api_key.py` file and run it (`python test_api_key.py`) in your active virtual environment. This script will list available models for your account. Look for models that support `generateContent` (e.g., `gemini-1.0-pro`, `text-bison-001`).
    * **How to change the model:**
        In `resume_generator.py`, locate the `generate_resume_section` function definition (e.g., `def generate_resume_section(section_name, user_input, model_name="gemini-pro"):`). You can change the default `model_name` parameter there, or modify the direct call to the `GenerativeModel` if you use different models for different sections. For example, if `text-bison-001` is available and you want to use it:
        `model = genai.GenerativeModel("text-bison-001")`

## Troubleshooting

* **`ModuleNotFoundError: No module named 'dotenv'` or `... 'google'` etc.:**
    This means the required Python packages are not installed in your active virtual environment.
    * Ensure your virtual environment is active (`(venv)` in your terminal prompt).
    * Run `pip install -r requirements.txt` again.
    * Verify installation with `pip list`.
    * In VS Code, confirm the correct Python interpreter (your `venv`'s interpreter) is selected in the bottom-left status bar.
* **`ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'`:**
    This means `requirements.txt` is either missing or you are not in the correct directory.
    * Ensure your terminal's current directory is your project's root folder (`ibm project python`). Use `cd <path_to_project_folder>`.
    * Verify that `requirements.txt` actually exists in that folder using the `dir` command (Windows) or `ls` (macOS/Linux). If not, create it as per the "Installation & Setup" steps.
* **`NotFound: 404 models/gemini-pro is not found...` or `No suitable text generation model found...`:**
    This indicates an issue with your Google API Key's access to Generative AI models.
    * **Your API key is likely valid, but the models themselves are not accessible.**
    * **Check Google AI Studio:** Log in to [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) with the account that owns the key.
    * **Check Google Cloud Console (if applicable):** Ensure the "Generative Language API" is enabled for your project and that quotas are not at zero. Some regions may not have certain models available yet.

---

Developed with love using Streamlit & Google Generative AI.# Resume-generator
