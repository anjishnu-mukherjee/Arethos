# FlipBit 

FlipBit is a web application designed to automate the grading of assessments. It accepts both text and image-based inputs and uses Gemini along with Pinecone to generate accurate scores along with personalized feedback. FlipBit reduces the evaluation burden for teachers and brings consistency to subjective assessments.

## Project Structure

```
Arethos/
├── react-app/        # React.js app (UI)
├── arethos-back/     # Python app (API & AI logic)
├── README.md
```

## Requirements

Before you begin, ensure the following tools are installed:

- Node.js (v18 or higher)
- Python 3.10 or higher

You’ll also need accounts and API keys for:

- Google Gemini API
- Pinecone Vector Database
- Azure 

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/anjishnu-mukherjee/Arethos.git
cd Arethos
```

### 2. Frontend Setup (React.js)

Navigate to the frontend folder:

```bash
cd react-app
```

Install dependencies:

```bash
npm install
```

Start the local server:

```bash
npm start
```

This will run the frontend on `http://localhost:3000`.

### 3. Backend Setup (Python)

Navigate to the backend folder:

```bash
cd ../arethos-back
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

For Installation of Azure Core tools Follow the link: [Install Azure Core Tool](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=linux%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-csharp)


Create a `.env` file in the `/arethos-back` directory with the following variables:

```
GEMINI_API_KEY=your_gemini_api_key
PINECONE_API_KEY=your_pinecone_api_key
AZURE_STORAGE_ACCOUNT_KEY=your_azure_storage_key
AZURE_STORAGE_ACCOUNT_NAME=your_account_name
```

Run the backend server:

```bash
func start
```

### 4. Connect Frontend with Backend

Update the following endpoints inside

- `src/UploadScreen.jsx` -> gemininResponse endoint

- `src/BlobStorage.jsx` -> sasurl endpoint

Save and reload the frontend.

## Development Team

Developed by Team Arethos

- Anjishnu Mukherjee
- Archit Anant

