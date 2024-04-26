import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/contacts.readonly'
]


def google_api(service_name: str):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build(service_name, 'v1', credentials=creds)

    return service

def google_people_api():
    google = google_api('people')
    contacts = google.people().connections().list(
        resourceName='people/me',
        personFields='names,emailAddresses,phoneNumbers'
    ).execute()
    data_to_create = []
    for contact in contacts.get('connections', []):
        names = contact.get('names', [])
        email_addresses = contact.get('emailAddresses', [])
        phone_numbers = contact.get('phoneNumbers', [])

        name = names[0].get('displayName', '') if names else ''
        email = email_addresses[0].get('value', '') if email_addresses else ''

        phone = phone_numbers[0].get('value', '') if phone_numbers else ''
        data_to_create.append({
            'name': name,
            'email': email,
            'phone': phone,
        })
    return data_to_create



def main():
    people =  google_people_api()
    print(people)

if __name__ == '__main__':
    main()