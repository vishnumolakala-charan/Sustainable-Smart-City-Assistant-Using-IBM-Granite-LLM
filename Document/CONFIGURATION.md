## 🔐 API Keys & Environment Configuration

To securely use external services like **IBM Watsonx Granite** and **Pinecone**, create a `.env` file in the root of your project.

---

### 🧾 .env Template

Create a `.env` file with the following structure:

```env
# ---------------------------
# IBM Watsonx Granite LLM
# ---------------------------
WATSONX_API_KEY=your_ibm_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_MODEL_ID=granite-13b-chat-v2 # or appropriate model

# ---------------------------
# Pinecone Vector Database
# ---------------------------
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=your_pinecone_environment_here
PINECONE_INDEX_NAME=sustainable-smartcity-index
```

> 🔒 **Note:** Never upload your `.env` file to GitHub. Make sure to add it to `.gitignore`.

---

### ✅ How to Get These Keys

#### 🔹 IBM Watsonx Granite (Watsonx.ai)

1. Log in to [IBM Cloud Console](https://cloud.ibm.com/)
2. Navigate to **Watsonx → Projects**
3. Copy your:

   * **API Key**
   * **Project ID**
   * **Model ID** (like `granite-13b-chat-v2`)

#### 🔹 Pinecone

1. Visit [https://app.pinecone.io](https://app.pinecone.io)
2. Create an account and a new **Index**
3. Copy your:

   * **API Key**
   * **Environment**
   * **Index Name**

---

### ✅ Python Integration (config.py)

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    watsonx_api_key: str
    watsonx_project_id: str
    watsonx_model_id: str
    pinecone_api_key: str
    pinecone_environment: str
    pinecone_index_name: str

    class Config:
        env_file = ".env"

settings = Settings()
```
