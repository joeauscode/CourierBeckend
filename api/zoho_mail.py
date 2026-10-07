import requests
from django.conf import settings


def get_zoho_access_token():
    response = requests.post(
        "https://accounts.zoho.com/oauth/v2/token",
        data={
            "refresh_token": settings.ZOHO_REFRESH_TOKEN,
            "client_id": settings.ZOHO_CLIENT_ID,
            "client_secret": settings.ZOHO_CLIENT_SECRET,
            "grant_type": "refresh_token",
        },
        timeout=20,
    )

    response.raise_for_status()

    data = response.json()

    if "access_token" not in data:
        raise RuntimeError(f"Zoho token error: {data}")

    return data["access_token"]


def send_zoho_email(to_email, subject, content, reply_to=None):
    access_token = get_zoho_access_token()

    url = f"https://mail.zoho.com/api/accounts/" f"{settings.ZOHO_ACCOUNT_ID}/messages"

    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    payload = {
        "fromAddress": settings.ZOHO_FROM_EMAIL,
        "toAddress": to_email,
        "subject": subject,
        "content": content,
    }

    if reply_to:
        payload["replyTo"] = reply_to

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()
