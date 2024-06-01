import pyshorteners
from flask import Flask, redirect, request
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

server = Flask(__name__)


SCOPES = ["https://www.googleapis.com/auth/classroom.announcements","https://www.googleapis.com/auth/classroom.courses"
          ,"https://www.googleapis.com/auth/classroom.coursework.me","https://www.googleapis.com/auth/classroom.coursework.students"
          ,"https://www.googleapis.com/auth/classroom.profile.emails","https://www.googleapis.com/auth/classroom.profile.photos"
          ,"https://www.googleapis.com/auth/classroom.student-submissions.me.readonly","https://www.googleapis.com/auth/classroom.push-notifications"]


flow = InstalledAppFlow.from_client_secrets_file(
    "credentials.json", 
    scopes = SCOPES
)

@server.route("/authorize")
def authorize():
  authorization_url, _ = flow.authorization_url(prompt="consent")
  print(authorization_url)
  return authorization_url
  

@server.route("/credentials")
def credentials():
  authorization_response = request.url
  flow.fetch_token(authorization_response=authorization_response)
  credentials = flow.credentials
  print("Access Token:", credentials.token)
  print("Refresh Token:", credentials.refresh_token)

  return "Authorization successful!"

if __name__ == '__main__':
  server.run(port = 500)