import os
import sys


def get_error_details(message,error_info:sys):
    _,_,tb=error_info.exc_info()
    filename=tb.tb_frame.f_code.co_filename
    line_no=tb.tb_lineno
    return f"Exception is found in filename {[filename]} at line number [{line_no}] with details as [{message}]"


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(self,error_message)
        self.error_mesage_detail=get_error_details(error_message,error_info=error_detail)

    def __str__(self):
        return self.error_mesage_detail