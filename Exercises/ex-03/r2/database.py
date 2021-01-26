import clients

class Database:
    def __init__(self):
        self.fields_description = clients.getFields()

    @staticmethod
    def new_obj_check(f_name,l_name,phone,email,startdate):
        try:
            test = clients.Client(f_name,l_name,phone,email,startdate)
        except ValueError as e:
            inputerror = e

            if inputerror == None:
                return None
            else:
                return e