# -*- coding: utf-8 -*-
"""The base Controller API."""
from myproject.lib.helpers import whoami
import os,sys
from tg import abort
__all__ = ['ExportCSV']

from pathlib import Path


class ExportCSV():
    """
     Export CSV
    """
    @classmethod
    def create(cls, list,name,url):
        cwd = os.getcwd()
        np=cwd.rfind("/")+1
        who=whoami()
        if who=="":
            error="CSV Failure"
            reason="User not logged"
            message = "The following {} occured, this is due to {}, please DEBUG the url : {}".format(error, reason,url)
            abort(status_code=500, detail=message)
        file_name=cwd+"/"+cwd[np:]+"/public/"+who+"_"+name+".csv"
        my_file = Path(file_name)
        if my_file.is_file():
            os.remove(file_name)
        outfile = open(file_name, 'w')
        for item in list:
            outfile.write(item)
        outfile.close()
        return "/"+who+"_"+name+".csv"
