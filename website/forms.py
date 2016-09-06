# _*_ coding:utf-8 _*_
from django import forms

class AddVideoDeviceForm(forms.Form):
    pid = forms.CharField()
    name = forms.CharField()
    group = forms.CharField()
    region = forms.CharField()
    direction = forms.CharField()
    vtype = forms.CharField()
    ip = forms.GenericIPAddressField(protocol='ipv4')
    username = forms.CharField()
    password = forms.CharField()
    gpslon = forms.CharField()
    gpswei = forms.CharField()

class AddDeviceStatusForm(forms.Form):
    devicestatus = forms.CharField()
class AddDeviceGroupForm(forms.Form):
    devicegroup = forms.CharField()
class AddDeviceRegionForm(forms.Form):
    deviceregion = forms.CharField()
class AddVideoDirectionForm(forms.Form):
    videodirection = forms.CharField()
class AddVideoTypeForm(forms.Form):
    videotype = forms.CharField()
class AddDeviceBrandForm(forms.Form):
    devicebrand = forms.CharField()
class AddDeviceTypeForm(forms.Form):
    devicetype = forms.CharField()