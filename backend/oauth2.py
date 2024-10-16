from fastapi import Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
import JWTtoken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
oauth2_staff = OAuth2PasswordBearer(tokenUrl="loginStaff")



def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return JWTtoken.verify_token(token,credentials_exception)
