import logging
import os
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions, BlobClient
import datetime
from datetime import timedelta
from dotenv import load_dotenv
import mimetypes

load_dotenv()
AZURE_STORAGE_ACCOUNT_NAME = os.environ["AZURE_STORAGE_ACCOUNT_NAME"]
AZURE_STORAGE_ACCOUNT_KEY = os.environ["AZURE_STORAGE_ACCOUNT_KEY"]
AZURE_BLOB_CONTAINER = "arethos"

blob_service_client = BlobServiceClient(account_url=f"https://{AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net", credential=AZURE_STORAGE_ACCOUNT_KEY)

def generate_sas_token(file_name):
    """Generate SAS Token for Azure Blob Storage upload."""
    try:
        sas_token = generate_blob_sas(
            account_name=AZURE_STORAGE_ACCOUNT_NAME,
            container_name=AZURE_BLOB_CONTAINER,
            blob_name=file_name,
            account_key=AZURE_STORAGE_ACCOUNT_KEY,
            permission=BlobSasPermissions(read=True, write=True),
            expiry=datetime.datetime.now(datetime.timezone.utc) + timedelta(hours=1)  # Expiry set to 1 hour
        )
        blob_url = f"https://{AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_BLOB_CONTAINER}/{file_name}?{sas_token}"
        return {"blob_url": blob_url, "sas_token": sas_token}
    except Exception as e:
        logging.error(f"Error generating SAS token: {e}")
        raise

def get_blob_data(sas_url):
    """Get blob data from Azure Blob Storage using SAS URL."""
    # sas_url = https://aristoragev01.blob.core.windows.net/arethos/test_file.pdf?se=2025-04-01T19%3A00%3A57Z&sp=w&sv=2025-05-05&sr=b&sig=prjpYe2ctiIY5Q%2Bpd75KrDgg8GATM9IaI7hipGZ4x4Y%3D

    file_name = sas_url.split("/")[-1].split("?")[0]  # Extract file name from URL
    print(sas_url)
    try:
        blob_client = BlobClient.from_blob_url(sas_url)
        blob_data = blob_client.download_blob().readall()
        save_path,file_type = save_blob_data(blob_data,file_name)
        return save_path, file_type
    except Exception as e:
        logging.error(f"Error retrieving blob data: {e}")
        raise


def save_blob_data(blob_data, file_name, output_dir="/tmp"):
    """Save blob data in the respective format."""
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    file_path = os.path.join(output_dir, file_name)
    mime_type, _ = mimetypes.guess_type(file_name)

    try:
        if mime_type and mime_type.startswith("image"):
            # Save as image (PNG, JPG, etc.)
            with open(file_path, "wb") as img_file:
                img_file.write(blob_data)
            return file_path, mime_type

        elif mime_type == "application/pdf":
            # Save as PDF
            with open(file_path, "wb") as pdf_file:
                pdf_file.write(blob_data)
            return file_path, mime_type

        elif mime_type and mime_type.startswith("text"):
            # Save as text file
            text_content = blob_data.decode("utf-8")  # Convert bytes to string
            with open(file_path, "w", encoding="utf-8") as text_file:
                text_file.write(text_content)
            return file_path, mime_type

        return None,None

    except Exception as e:
        return None,None
