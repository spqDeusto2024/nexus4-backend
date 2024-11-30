import jwt
from datetime import datetime, timedelta
from typing import Dict
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.utils.vars import SECRET_KEY, ALGORITHM  


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  

def create_access_token(data: Dict[str, str], expires_in: timedelta = timedelta(hours=1)) -> str:
    """
    Crea un JWT para el usuario.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_in
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> dict:
    """
    Verifica un JWT y devuelve los datos del usuario.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"Payload decodificado: {payload}")  # Depuración
        return payload
    except jwt.ExpiredSignatureError:
        print("El token ha expirado")  # Log adicional
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El token ha expirado."
        )
    except jwt.JWTError as e:
        print(f"Error al decodificar el token: {e}")  # Log adicional
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido."
        )

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Dependencia que extrae el token JWT de la solicitud y valida al usuario.
    """
    print("Dentro de get_current_user") 
    try:
        print(f"Token recibido: {token}")  # Depuración
        payload = verify_token(token)  # Decodifica y valida el token
        print(f"Payload decodificado: {payload}")  # Depuración
        return payload
    except HTTPException as e:
        print(f"Error al autenticar: {e.detail}")
        raise e
    except Exception as ex:
        print(f"Error inesperado: {ex}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error procesando el token",
        )