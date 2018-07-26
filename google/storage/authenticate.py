from google.cloud import storage

# Using credentials in file specified by GOOGLE_APPLICATION_CREDENTIALS environment variable.

storage_client = storage.Client()
buckets = list(storage_client.list_buckets())
print(f"Buckets: {buckets}")

