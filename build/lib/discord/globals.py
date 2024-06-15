from typing import Optional, Any, Dict

GLOBALS: Dict[str,Any] = {}

def set_global(key: str, value: Any) -> bool:
    GLOBALS[key] = value
    return True

def get_global(key: str, default: Optional[Any] = None) -> Optional[Any]:
    return GLOBALS.get(key, default)