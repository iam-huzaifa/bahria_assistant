# Reads secrets from .env locally, and from Streamlit Secrets on Streamlit Cloud.
# On Streamlit Cloud there is no .env file, so add these 4 keys in
# Streamlit Cloud -> App settings -> Secrets (TOML format):
#   DATABASE_URL = "..."
#   GOOGLE_API_KEY = "..."
#   SUPABASE_URL = "..."
#   SUPABASE_SERVICE_ROLE_KEY = "..."
import os
from dotenv import load_dotenv

load_dotenv()


def _get_secret(name):
    value = os.getenv(name)
    if value:
        return value
    try:
        import streamlit as st

        return st.secrets.get(name)
    except Exception:
        return None


DATABASE_URL = _get_secret("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is missing - set it in .env locally or in Streamlit Secrets on Streamlit Cloud")

GOOGLE_API_KEY = _get_secret("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing - set it in .env locally or in Streamlit Secrets on Streamlit Cloud")

SUPABASE_URL = _get_secret("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = _get_secret("SUPABASE_SERVICE_ROLE_KEY")

if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    raise ValueError("Supabase credentials are missing - set them in .env locally or in Streamlit Secrets on Streamlit Cloud")
