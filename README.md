# Instagram feed smart filter
Web client for instagram feed which shows media that has filtered objects in it (currently only cats)
### Installation and Usage:
Before anything you can clone the repository using:
```
git clone https://github.com/Vlsarro/instafeed-smart-filter
```
#### Install required packages
Install packages from requirements to start the application
```bash
pip install -r requirements.txt
```

#### Usage
Create `user_data.json` file to set Instagram user id (you can find it out by account name using some tools like here https://codeofaninja.com/tools/find-instagram-user-id). Use following format:
```json
{"instagramUserId": 4042252094}
```
Use python to run the application.
```bash
python app.py
```  
