import logging
import os
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions, BlobClient
import datetime
from datetime import timedelta
from dotenv import load_dotenv
import shutil
from urllib.parse import urlparse, unquote

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
    parsed_url = urlparse(sas_url)
    file_name = os.path.basename(parsed_url.path)
    file_name = unquote(file_name)  # Decode %20 etc.

    print(f"Extracted file_name: {file_name}")

    try:
        blob_client = BlobClient.from_blob_url(sas_url)
        blob_data = blob_client.download_blob().readall()
        save_path, file_type = save_blob_data(blob_data, file_name)
        return save_path, file_type
    except Exception as e:
        logging.error(f"Error retrieving blob data: {e}")
        raise


def save_blob_data(blob_data, file_name, output_dir="/tmp"):
    """Save blob data based on file extension check."""
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, file_name)

    try:
        if ".txt" in file_name.lower():
            mime_type = "text/plain"
            text_content = blob_data.decode("utf-8")
            with open(file_path, "w", encoding="utf-8") as text_file:
                text_file.write(text_content)

        elif ".pdf" in file_name.lower():
            mime_type = "application/pdf"
            with open(file_path, "wb") as pdf_file:
                pdf_file.write(blob_data)

        elif any(ext in file_name.lower() for ext in [".jpeg", ".jpg", ".png"]):
            mime_type = "image/*"
            with open(file_path, "wb") as img_file:
                img_file.write(blob_data)

        else:
            mime_type = "application/octet-stream"
            with open(file_path, "wb") as bin_file:
                bin_file.write(blob_data)

        print(f"Saved file: {file_path}, mime_type: {mime_type}")
        return file_path, mime_type

    except Exception as e:
        print(f"Failed to save blob data: {e}")
        return None, None


def clean_tmp(output_dir="/tmp"):
    """Remove all files from /tmp."""
    try:
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
            print(f"/tmp cleaned successfully.")
    except Exception as e:
        print(f"Failed to clean /tmp: {e}")
