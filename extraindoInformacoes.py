import requests

url = "https://api.rd.services/platform/segmentations/13222691/contacts"

headers = {
    "accept": "application/json",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaS5yZC5zZXJ2aWNlcyIsInN1YiI6ImxaRkhiSVRla1JhMmdSZFRjOXJmTV9aRGN6WlpQZDBsSzZEZ3B5MjNpYWNAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vYXBwLnJkc3RhdGlvbi5jb20uYnIvYXBpL3YyLyIsImFwcF9uYW1lIjoiQ29uZ3Jlc3NvMjAyNCIsImV4cCI6MTcyMTMxNTYyNiwiaWF0IjoxNzIxMjI5MjI2LCJzY29wZSI6IiJ9.zKO_riEKGjCLqjYfiB-lOxWnAXrF2m0QHK14AWFwrJa2cu2kJQdE77zBzdYM8u1FGrk2lurZWh-XM37frba9hgmA954p0dhU28ZCNa5s83yijyAng7ON15Hu5DymWqD6XAhy5FgKQljlTJd3AUZ8f3F6OwZHFpkHUZBHh8Ea7R6g56sahEqGwJJChNt1LabAA05gsEJ7227NO15MnbEc-l84_M7i8BQxVRHGRq_rTH0v2ZTK6dtrluCgDXaQ3BSWbPL3OFp8z8sxmwTn00ASL6qnKaXBSZzCpQ3B2pfXnimYb56QABrwsSFJevb3cfruIS5WgsYbS28GiO5KJlZb7A"
}

response = requests.get(url, headers=headers)

print(response.text)