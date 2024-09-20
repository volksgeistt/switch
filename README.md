# Switch - Discord Status Shifter
![image](https://github.com/user-attachments/assets/8bf02b2f-0196-46a7-a756-7dc9d109f6c5)
## Features
- **Supports Multiple Accounts / Tokens**
- **Updates Status Text & Status Presence Too ~ ( IDLE / DND / ONLINE )**
- **Fully Customizable Config Settings**
- **Easy To Use userInterface & setupMenu**
## Setup
- **Download the files above**
- **Browse the in your directory**
- **Open `userAccounts.json` file and setup your config**
- **Save it and run the `start.bat` file from the
## userAccounts Config Setup Example
```json
{
    "accounts": [
      {
        "userToken": "ABC1234567.DEFghIJK.LMNoPqrStUv",
        "settingsList": [
          {"custom_status": {"text": "Code"}, "status": "online"},
          {"custom_status": {"text": "Game"}, "status": "idle"},
          {"custom_status": {"text": "Work"}, "status": "dnd"}
        ]
      }
    ],
    "interval": 10
  }```
