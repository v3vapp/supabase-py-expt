from storage3 import create_client
import config

headers = {"apiKey": config.key, "Authorization": f"Bearer {config.key}"}

# pass in is_async=True to create an async client
storage_client = create_client(config.storage_url, headers, is_async=False)

storage_client.list_buckets()