# encoding: utf-8

"""
File: custom_site.py
Author: Rock Johnson
"""
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea 管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
