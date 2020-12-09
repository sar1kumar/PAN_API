# PAN_API
An API using Flask-Restex, python ORM MongoDB, Flask-JWT-Extended for managing authentication using JWT Bearer tokens.
You will give a PAN Number as the input to the API, and returns the details after validating the PAN Number.

## Validation of PAN Number ##
The valid PAN Card number must satisfy the following conditions: 


  *  It should be ten characters long.
  *  The first five characters should be any upper case alphabets.
  *  The next four-characters should be any number from 0 to 9.
  *  The last(tenth) character should be any upper case alphabet.
  *  It should not contain any white spaces

```python
    # Python code for Pan Validation in API
    def validate_pan_number(pan_number):
    # Validates if the given value is a valid PAN number or not, if not raise ValidationError
    if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', str(pan_number)):
        return pan_number
    else:
        abort(400, 'ValidationError')
```
## PAN API ##

Install the required modules and dependencies and run app.py file.


### Installations ###

* INSTALL **POSTMAN**
* Execute the following commands in the Terminal   #Linux

```bash
pip install -r requirements.txt
```


```bash
cd ~/api
python app.py
```


![IMG](https://github.com/sar1kumar/PAN_API/blob/main/pics/Screenshot_2020-12-09%20PAN%20DATA%20API.png)

Install POSTMAN to test the API

* Send a POST Requet to https://127.0.0.1:5000/auth/signup
* Enter the body of the reuest in json format with the required details.
      
      {
        "email": "example@email.com",
        "password" : "EXAMPLE",
        "name" : "SOME NAME"
      }
* Click on Send.
* You will recieve a client-id in the following format. This client id is used for getting pan details.

      {
        "result":{
          "id": "5fd07b96746195df13501ff2"
        }
      }
      
![IMG](https://github.com/sar1kumar/PAN_API/blob/main/pics/Screenshot%20from%202020-12-09%2012-54-13.png)


* Send a POST Request https://127.0.0.1:5000/auth/login
* Enter the body of the reuest in json format with the required details.
* Click on send.

      {    
        "email": "test@gmail.com",
        "password": "mypass"        
      }
* You will Receive access token which is used for authentication while recieving PAN details.

      {
       "result": {
       "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDc0OTg3MjcsIm5iZiI6MTYwNzQ5ODcyNywianRpIjoiMDkwMGI2OGUtN2ZkOS00YzNlLWJjNGEtMzdjMmViNTcxZWMwIiwiZXhwIjoxNjA3OTMwNzI3LCJpZGVudGl0eSI6IjVmZDA3Yjk2NzQ2MTk1ZGYxMzUwMWZmMiIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.SVpN2scwPp8v7WsOZ8MSeo2gZSNle65eRyM8k4fNPsI", 
      "logged_in_as": "test@gmail.com", 
      "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDc0OTg3MjcsIm5iZiI6MTYwNzQ5ODcyNywianRpIjoiNzU3N2Y4ZjQtYTdlNS00MDUzLTllNDEtOWM3ZWFkOTVmYjVkIiwiZXhwIjoxNjEwMDkwNzI3LCJpZGVudGl0eSI6IjVmZDA3Yjk2NzQ2MTk1ZGYxMzUwMWZmMiIsInR5cGUiOiJyZWZyZXNoIn0.c4SvW3KDIlNn5bWhCpTjZC-oxLQ2cq1hvZHnEb2BWMM"
                }
      }↵

![IMG](https://github.com/sar1kumar/PAN_API/blob/main/pics/Screenshot%20from%202020-12-09%2012-55-40.png)

* Send a GET request to https://127.0.0.1:5000/{pan_number}/{client_id}
* Click on the AUTHENTICATION section in POSTMAN requests and select BEARER TOKEN you have received the BEARER Token or access token after the login request as the result copy and paste it in the Token Field
* Enter the pan number in the place of {pan_number} and replace {client_id} with the received client id which you have received after the Signup Request
* Click on Send.
* You will Receive the PAN details as the result.
      
      {
           "result" : {
            'pan': pan_number,
        'name': 'Dinesh Kumar',
        'dob': '25-10-1990',
        'father_name': 'Hari Kumar',
        'clientid': cid
         }
      }

![IMG](https://github.com/sar1kumar/PAN_API/blob/main/pics/Screenshot%20from%202020-12-09%2012-50-54.png)


### MONGO DB ###

* Used the Cloud Atlas: MongoDb for storing and accessing the data.
* The Data is be persisted in MongoDB using the mongoengine library.
* Date of birth("dob" field) is stored as DateTimeField in Mongo, and is serialized in JSON output in the format YYYY-MM-DD
* There are two main collections, for User collection for which token would be generated, and a PanClient collection which will be related to the User collection. For each new verification request a new client with client_id will be generated.

![IMG](https://github.com/sar1kumar/PAN_API/blob/main/pics/Screenshot%20from%202020-12-09%2013-25-34.png)
