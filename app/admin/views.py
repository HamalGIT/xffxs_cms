#conding:utf8
from . import  admin

@admin.route("/")
def index():
    return  "admin index";