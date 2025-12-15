from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from supabase import create_client
from app.core.config import SUPABASE_URL, SUPABASE_KEY

security = HTTPBearer()
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_current_user(token = Depends(security)):
    try:
        user = supabase.auth.get_user(token.credentials)
        return user.user
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
