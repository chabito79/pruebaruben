# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ruben"
app_title = "Ruben"
app_publisher = "TOTALL"
app_description = "App demo de Ruben"
app_icon = "octicon octicon-device-camera"
app_color = "red"
app_email = "admin@totall.mx"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ruben/css/ruben.css"
# app_include_js = "/assets/ruben/js/ruben.js"

# include js, css files in header of web template
# web_include_css = "/assets/ruben/css/ruben.css"
# web_include_js = "/assets/ruben/js/ruben.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ruben.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ruben.install.before_install"
# after_install = "ruben.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ruben.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ruben.tasks.all"
# 	],
# 	"daily": [
# 		"ruben.tasks.daily"
# 	],
# 	"hourly": [
# 		"ruben.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ruben.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ruben.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ruben.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ruben.event.get_events"
# }

