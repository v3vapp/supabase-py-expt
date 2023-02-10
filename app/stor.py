from supabase import create_client, Client
import config

#############################################################
# SUPABASE STORAGE IS USELESS. USE AWS-S3 OR GCP-CGS.
#############################################################


supabase: Client = create_client(config.url, config.key)

file = open("test.png", "rb")

response = supabase.files.upload(file, filename="file.jpg")

if response.status_code == 200:
    print("File uploaded successfully!")
else:
    print("File upload failed with status code: ", response.status_code)