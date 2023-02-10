
import os
import config
from supabase import create_client, Client
import json

supabase: Client = create_client(config.url, config.key)

country_data = supabase.table('countries').select('*').execute().data # fetching documents

print(country_data)



