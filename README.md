# Smart ATS

Smart ATS is an Applicant Tracking System (ATS) designed to analyze resumes against job descriptions. Utilizing the Google Gemini Pro API and Streamlit, this tool provides actionable insights, including JD match percentage, missing keywords, CV score, and suggestions for improvement.

## Features

- **Resume Analysis**: Extracts and evaluates text from PDF resumes.
- **Job Description Comparison**: Matches resume content with job descriptions.
- **Detailed Insights**: Offers JD match percentage, missing keywords, CV score, and improvement suggestions.
- **Interactive Interface**: Developed with Streamlit for user-friendly interaction.

## Technologies Used

- **Streamlit**: Framework for the web application interface.
- **Google Gemini Pro API**: For advanced content analysis and generative AI capabilities.
- **PyPDF2**: Library for extracting text from PDF files.
- **Python**: Language used for developing the application.

## Installation

### Prerequisites

- Python 3.8 or later
- Google Gemini Pro API key
- PDF files for resumes

### Steps

1. **Clone the Repository:**


   git clone https://github.com/yourusername/smart-ats.git
   cd smart-ats
2. **Create and Activate a Virtual Environment:**

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies:**

pip install -r requirements.txt

4. **Set Up Environment Variables:**

Create a .env file in the project root and add your API key:

GOOGLE_API_KEY=your_google_gemini_pro_api_key

## Usage

1. **Run the Streamlit Application:**

streamlit run app.py

2. **Access the Application:**

Open your browser and go to `http://localhost:8501`.

3. **Interact with the Application:**

- Job Description: Paste the job description into the text area.
- Resume Upload: Upload your resume in PDF format.
- Submit: Click "Submit" to analyze the resume and view the results.

## Example

1. **Job Description Input:**

Senior Software Engineer
- Experience with Python and Django
- Knowledge of data structures and algorithms
- Strong problem-solving skills

2. **Resume Upload:**

Upload a PDF resume file.

3. **Results Displayed:**

- JD Match Percentage
- Missing Keywords
- Profile Summary
- CV Score
- Things that Can Be Improved in CV
- Skills Improvement Suggestions

## Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository.**
2. **Create a Feature Branch.**
3. **Commit Changes.**
4. **Push to Your Fork.**
5. **Open a Pull Request.**

## License
This project is licensed under the MIT License. 

## Contact
For questions or feedback, please reach out to `parmeetsingh1313n@gmail.com`.
