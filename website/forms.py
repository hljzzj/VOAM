# _*_ coding:utf-8 _*_

from django import forms
from django.forms import ModelForm
from models import *

class AddVideoDeviceForm(forms.Form):
    pid = forms.CharField(required=False,label='编号') # required=False允许为空
    name = forms.CharField(label='名称')
    group_list = DeviceGroup.objects.all()
    print group_list
    group = forms.ModelChoiceField(queryset=DeviceGroup.objects.all(),required=True,label=u'分组')

    region = forms.CharField()
    direction = forms.CharField()
    vtype = forms.CharField()
    brand = forms.CharField()
    dtype = forms.CharField()
    ip = forms.GenericIPAddressField(protocol='ipv4')
    username = forms.CharField(required=False)
    password = forms.CharField(required=False)
    gpslon = forms.CharField(required=False)
    gpswei = forms.CharField(required=False)
    telecom = forms.CharField()
    nvrdevice = forms.CharField(required=False)

class UpdateVideoDeviceForm(forms.Form):
    pid = forms.CharField(required=False) # required=False允许为空
    name = forms.CharField()
    group = forms.CharField()
    region = forms.CharField()
    direction = forms.CharField()
    vtype = forms.CharField()
    brand = forms.CharField()
    dtype = forms.CharField()
    ip = forms.GenericIPAddressField(protocol='ipv4')
    username = forms.CharField(required=False)
    password = forms.CharField(required=False)
    gpslon = forms.CharField(required=False)
    gpswei = forms.CharField(required=False)
    telecom = forms.CharField()


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