# Instagram cat feed test task
Web client for instagram feed which shows media that has cats in it
### Installation and Usage:
Before anything you can clone the repository using:
```
git clone https://github.com/Vlsarro/instacatfeed-test-task
```
#### Install required packages
Install packages from requirements to start the application
```bash
pip install -r requirements.txt
```

#### Usage
Create `user_data.json` file to set Instagram user id (you can find it out by account name using some tools like here https://codeofaninja.com/tools/find-instagram-user-id). For example:
```json
{"instagramUserI": 1403410255}
```
Use python to run the application.
```bash
python app.py
```
#### Additional comments
I did not have enough time to implement all the functionality from the task. I need to add caching, add logging instead of print expressions, add loading images from accounts that user is following. I also should write some tests for this application.

Currently this application only supports image filtration from the account specified in `user_data.json`.  