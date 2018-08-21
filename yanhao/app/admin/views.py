from . import admin
from flask import render_template,redirect,url_for,flash,session,request
from app.admin.forms import LoginForm
from app.models import Admin

@admin.route("/")
def index():
    return render_template("admin/index.html")

@admin.route("/login/",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if not admin.check_pwd(data["pwd"]):
            flash("密码错误！", 'err')
            return redirect(url_for("admin.login"))
        session["admin"] = data["account"]

        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html",form=form)

#退出
@admin.route("/logout/")
def logout():
    return redirect(url_for("admin.login"))

#修改密码
@admin.route("/pwd/")
def pwd():
    return render_template("admin/pwd.html")

@admin.route("/tag/add/")
def add():
    return render_template("admin/tag_add.html")

@admin.route("/tag/list/")
def list():
    return render_template("admin/tag_list.html")