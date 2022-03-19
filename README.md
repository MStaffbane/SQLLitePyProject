# SQLLitePyProject
My First Working Prototype using a combination of SQL and Python

## Description

The SQLLitePyProject is a short simple Python Program which allows you to view, edit and delete rows from a basic database using sqllite. 
This shall also recreate the data in order to show that not only is the data easy to store, but also maintain if something went wrong.
Note: Your data will be stored locally.

## Contents

- [First Time Running Instructions](#First-Time-Running-Instructions)
- [Tutorial and Screenshots](#Tutorial-and-Screenshots)
- [Features](#Features)
- [Preview Video](#Preview-Video)
- [Bugs and Fixes](#Bugs-and-Fixes)

# Preview
![image](https://user-images.githubusercontent.com/42208427/158641965-20c6db41-4247-4cb5-b1a5-72ea08565b5b.png)

# Preview Video
https://user-images.githubusercontent.com/42208427/158829214-d88e7c04-11c0-4694-b56d-38c73e844006.mp4

### Bugs and Fixes

As of 19th of March 2022: some bug fixes are to be patched... I will look into the compatibility and portability of this project and will patch this in a later version, but for now it seems functional I will look at if a person requires SQLlite to be installed or not in order to verify the program is functioning as it should.

A deployed version (for non-programmers) of this could be looked at at a later date.

#### Known Bugs

- Minor Clear Screen issues (Screen clears to be optimised to clear only at appropriate times)
- Video could be re-recorded and test cases more carefully used

#### Possible Improvements

- Coloured Error Prompts (A Pale Red Font if possible)
- Clear message prompts if 5 errors in a row have occured... although this could improve software friendlyness it could be hard to implement

#### Fixes
- Better User Interface Responsiveness
- Message Menus appear correctly (clearing the main menu so as not to have redeundancy)
- Minor SQL syntax errors
- Care has been taken to make sure the command calls are sequenced correctly in code

### First Time Running Instructions

Simply run Command 6:

![image](https://user-images.githubusercontent.com/42208427/158633701-7222b7d7-1420-4890-a1d1-6e9f2c33a973.png)

This will then prompt you:
![image](https://user-images.githubusercontent.com/42208427/158633908-ad62a8e6-9143-4038-8373-c9e88f49ee32.png)

Simply enter yes and the data will be reset or created for first time use (If at anytime you wish to reset to default values just follow this section again)

### Tutorial and Screenshots

Simply follow on screen prompts included within the program (e.g. Enter 1 to show all records)

Note: A first time run is required before use of this program - if this has been followed the program should run without issue.

![image](https://user-images.githubusercontent.com/42208427/158637412-a8b5a312-1542-450b-905d-e18f7f54f989.png)
![image](https://user-images.githubusercontent.com/42208427/158637568-17162415-eb16-4276-ab17-cbb942519604.png)
![image](https://user-images.githubusercontent.com/42208427/158637621-f1022f72-d53d-4e7b-b7b1-dcb418ad3dde.png)
![image](https://user-images.githubusercontent.com/42208427/158637778-8c01c54b-5fba-4ead-974c-4a4666e63584.png)
![image](https://user-images.githubusercontent.com/42208427/158637839-21118ab8-f9e1-4f16-9fc1-b1f00f7ee5c7.png)
![image](https://user-images.githubusercontent.com/42208427/158637918-3b738cd8-e46e-4d06-b497-acbb77086a70.png)
![image](https://user-images.githubusercontent.com/42208427/158638055-0978e11c-6abf-4793-9ba2-0c265129516c.png)
![image](https://user-images.githubusercontent.com/42208427/158638148-85adcd3d-6243-47c6-940d-27c7528c6079.png)
![image](https://user-images.githubusercontent.com/42208427/158638287-b87b07f5-0e17-4665-ab00-c2499c1bec71.png)
![image](https://user-images.githubusercontent.com/42208427/158638354-57146894-de38-43b3-a566-66d75faf0b33.png)
![image](https://user-images.githubusercontent.com/42208427/158638949-6e588451-4e1c-4ea2-9120-50588acc37f4.png)
![image](https://user-images.githubusercontent.com/42208427/158639282-b42ccc9c-5fff-4995-a590-955aa6c9e89c.png)
![image](https://user-images.githubusercontent.com/42208427/158640422-e4fb88f4-4334-45cc-b7ba-1f5e8c49cb60.png)
![image](https://user-images.githubusercontent.com/42208427/158640539-591f7abf-552f-48a6-b98c-70f262a344cc.png)
![image](https://user-images.githubusercontent.com/42208427/158640605-48f82811-821b-461d-9c6e-1b6c1f3d4545.png)

### Features:
- Displays Database Records
- Allows User to add own Record
- Allows User to delete a Record
- Search Feature
  - By ID
  - By First Name
  - By Last Name
  - By Email
- Allows User to ammend a Record
- Allows User to Reset or Create the Database
- Exits the Program
