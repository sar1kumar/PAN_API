from mongoengine import Document, StringField, DateTimeField,DateField


class PAN_details(Document):

    pan = StringField()
    name = StringField(required=True)
    father_name = StringField()
    DOB = DateField()
    clientid = StringField()
