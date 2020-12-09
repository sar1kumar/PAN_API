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
### PAN API ###

Install the required modules and dependencies and run api.py file.

![IMG](https://github.com/sar1kumar/PAN_API/blob/main/pics/Screenshot_2020-12-09%20PAN%20DATA%20API.png)
