import re


def verify_url_format(url: str) :
    regex = re.compile(
        r"^https:\/\/"  # Vérifie que l'URL commence par https://
        r"(?:(?:[A-Z0-9-]+\.)+[A-Z]{2,6}|"  # Domaine
        r"localhost|"  # ou localhost
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ou une IP (IPv4)
        r"(?::\d+)?"  # Port optionnel
        r"(?:\/\S*)?$",
        re.IGNORECASE,
    )
    regex2 = re.compile(
        r"^https:\/\/"  # Vérifie que l'URL commence par https://
        r"(?:bit\.ly|tinyurl\.com|tiny\.cc)"  # Vérifie que le domaine est bit.ly, tinyurl.com ou tiny.cc
        r"(?:\/\S*)?$",  # Chemin optionnel
        re.IGNORECASE,
    )

    if not re.match(regex, url):
        return {"message": "URL is not valid", "res": False}
    if re.match(regex2, url):
        return {"message": "URL is already shortened", "res": False}
    return {"message": "URL is valid", "res": True}
