import sys
from src.logger import logging


def message_details_error(error, error_details: sys):
    #select track
    exc_type, exc_obj, exc_tb = error_details.exc_info()
    #find file contain error
    file_name = exc_tb.tb_frame.f_code.co_filename
    #message contain file name (contain error), num line ,error
    error_message = "The error occurred in script [{0}] at line [{1}]: [{2}]".format(file_name, exc_tb.tb_lineno, str(error))

    return error_message







class CustomException(Exception):#تكتب في دفتر الأعطال
    def __init__(self, error_message, error_details: sys):           
        super().__init__(error_message)                 
        self.error_message = message_details_error(error_message, error_details)

    def __str__(self): #convert obj to string 
        return self.error_message