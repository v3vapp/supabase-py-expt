from dotenv import load_dotenv

load_dotenv()

import os

url: str = os.getenv("SUPABASE_URL")
storage_url: str = os.getenv("SUPABASE_STORAGE_URL")
key: str = os.getenv("SUPABASE_KEY")
sec: str = os.getenv("SUPABASE_SEC")
