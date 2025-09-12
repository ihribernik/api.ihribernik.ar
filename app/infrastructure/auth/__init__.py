from __future__ import annotations

from datetime import datetime, timedelta, timezone

from jose import ExpiredSignatureError, JWTError, jwt

from app.infrastructure.config import Settings

settings = Settings()

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS


class JWTService:
    @staticmethod
    def create_access_token(
        data: dict,
        expires_delta: timedelta | None = None,
    ) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + (
            expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        to_encode.update({"exp": expire, "type": "access"})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def create_refresh_token(
        data: dict,
        expires_delta: timedelta | None = None,
    ) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + (
            expires_delta or timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        )
        to_encode.update({"exp": expire, "type": "refresh"})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def verify_token(token: str, expected_type: str = "access") -> dict | None:
        """
        expected_type puede ser "access" o "refresh"
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            if payload.get("type") != expected_type:
                return None
            return payload
        except ExpiredSignatureError:
            return None  # Token expirado
        except JWTError:
            return None  # Token inválido

    @staticmethod
    def refresh_access_token(refresh_token: str) -> str | None:
        """
        Recibe un refresh token válido y genera un nuevo access token.
        """
        payload = JWTService.verify_token(refresh_token, expected_type="refresh")
        if not payload:
            return None

        # Eliminar campos viejos que no corresponden
        sub = payload.get("sub")
        if not sub:
            return None

        return JWTService.create_access_token({"sub": sub})
