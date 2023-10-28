# GitSeek
First task of Web/Cloud members of GDSC NITS 2026

# Guide to Run it Locally
- Install all the packages mentioned in requirements.txt via the command $pip install -r requirements. txt
- Change this piece of code in app.py, line number 14 to 17
  ```
  github_api_url = os.environ["GITHUB_API_URL"]
  github_access_token = os.environ["GITHUB_ACCESS_TOKEN"]
  response = requests.get(f"{github_api_url}/users/{name}", headers={"Authorization": f"Bearer {github_access_token}"})
  ```
- To
  ```
  response = requests.get(f"https://api.github.com/users/{name}")
  ```
- Now use flask run to run it locally!
