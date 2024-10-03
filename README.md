# eater_scraper
Description: Scrapes info from Eater's restaurant lists which then populates a Google spreadsheet. Done out of laziness for researching food places in a new city.

Follow the instructions here to set up your own Google Sheets API: https://www.makeuseof.com/tag/read-write-google-sheets-python/. You'll create a private key in JSON format which you will need to save to your own local environment. I named my JSON file "eater-scraper-key.json".

'''
{
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "",
  "universe_domain": "googleapis.com"
}
'''


