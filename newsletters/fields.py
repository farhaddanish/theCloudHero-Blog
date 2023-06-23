from django.db import models




class LowerEmailField (models.EmailField):
    def __init__(self,*args, **kwargs):
        super(LowerEmailField,self).__init__(*args, **kwargs)

    def from_db_value (self,value,expression, connection):
        if value is None:
            return value
        return value.lower()

    def get_prep_value(self, value) :
        value =  super(LowerEmailField,self).get_prep_value(value)
        return value.lower()