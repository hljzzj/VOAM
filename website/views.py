# _*_ coding: utf-8 _*_
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from website.forms import AddVideoDeviceForm,AddDeviceStatusForm,AddDeviceGroupForm,AddDeviceRegionForm,AddVideoDirectionForm,AddVideoTypeForm,AddDeviceBrandForm,AddDeviceTypeForm
from website.models import DeviceStatus,DeviceGroup,DeviceRegion,VideoDirection,VideoType,DeviceBrand,DeviceType,ServerHostDevice,VideoDevice,NVRDevice,NetworkDevice

def Index(request):
    good_serverlist = ServerHostDevice.objects.filter()
    bed_serverlist = ServerHostDevice.objects.filter()

def AddBasicInfo(request):
    devicestatusform = AddDeviceStatusForm()
    devicegroupform = AddDeviceGroupForm()
    deviceregionform = AddDeviceRegionForm()
    videodirectionform = AddVideoDirectionForm()
    videotypeform = AddVideoTypeForm()
    devicebrandform = AddDeviceBrandForm()
    devicetypeform = AddDeviceTypeForm()
    devicebrandid = DeviceBrand.objects.all()
    if request.method == 'POST':
        if request.POST.get('devicestatus') != 0:
            devicestatus = AddDeviceStatusForm(request.POST)
            if devicestatus.is_valid():
                devicestatus = request.POST.get('devicestatus')
                result = DeviceStatus.objects.filter(devicestatus=devicestatus).count()
                if result == 0:
                    DeviceStatus.objects.create(devicestatus=devicestatus)
                    return render_to_response('AddBasicInfo.html',{'devicestatusform': devicestatusform,'devicegroupform':devicegroupform,'deviceregionform':deviceregionform,'videodirectionform':videodirectionform,'videotypeform':videotypeform,'devicebrandform':devicebrandform,'devicetypeform':devicetypeform,'devicebrandid':devicebrandid,'devicestatus':'添加成功'})
                else:
                    return render_to_response('AddBasicInfo.html', {'devicestatusform': devicestatusform,'devicegroupform':devicegroupform,'deviceregionform':deviceregionform,'videodirectionform':videodirectionform,'videotypeform':videotypeform,'devicebrandform':devicebrandform,'devicetypeform':devicetypeform,'devicebrandid':devicebrandid,'devicestatus':'已存在'})
            else:
                return render_to_response('AddBasicInfo.html', {'devicestatusform': devicestatusform,'devicegroupform':devicegroupform,'deviceregionform':deviceregionform,'videodirectionform':videodirectionform,'videotypeform':videotypeform,'devicebrandform':devicebrandform,'devicetypeform':devicetypeform,'devicebrandid':devicebrandid})


    else:
        return render_to_response('AddBasicInfo.html', {'devicestatusform': devicestatusform,'devicegroupform':devicegroupform,'deviceregionform':deviceregionform,'videodirectionform':videodirectionform,'videotypeform':videotypeform,'devicebrandform':devicebrandform,'devicetypeform':devicetypeform,'devicebrandid':devicebrandid})




def AddVideoDevice(request):
    addvideodevice = AddVideoDeviceForm()
    if request.method == 'POST':
        form = AddVideoDevice(request.POST)
        if form.is_valid():
            pid = request.POST.get('pid')
            name = request.POST.get('name')
            group = request.POST.get('group')
            region = request.POST.get('region')
            vtype = request.POST.get('vtype')
            ip = request.POST.get('ip')
            username = request.POST.get('username')
            password = request.POST.get('password')
            gpslon = request.POST.get('gpslon')
            gpswei = request.POST.get('gpswei')
            result = VideoDevice.objects.filter(ip=ip).count()
            result1 = VideoDevice.objects.filter(pid=pid).count()
            if result == 0 and result1 == 0:
                VideoDevice.objects.create(pid=pid,name=name,group=group,region=region,vtype=vtype,ip=ip,username=username,password=password,gpslon=gpslon,gpswei=gpswei)
                return render_to_response('AddVideoDevice.html',{'form':addvideodevice,'status':'添加成功'})
            elif result != 0:
                return render_to_response('AddVideoDevice.html', {'form': addvideodevice, 'status': 'IP已存在'})
            else:
                return render_to_response('AddVideoDevice.html',{'form':addvideodevice,'status':'ID已存在'})
        else:
            return render_to_response('AddVideoDevice.html', {'form': addvideodevice})
    else:
        return render_to_response('AddVideoDevice.html', {'form': addvideodevice})



