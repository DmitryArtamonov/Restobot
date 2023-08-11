import re
import string

def clean_string(text: str):
    """Change nonstandard symbols with '*' to prevent errors when print()"""

    pattern = f"[^{re.escape(string.printable)}]"

    cleaned_string = re.sub(pattern, '*', text)

    return cleaned_string