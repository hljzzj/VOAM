# coding:utf-8
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
        devicestatus = request.POST.get('devicestatus')
        devicegroup = request.POST.get('devicegroup')
        deviceregion = request.POST.get('deviceregion')
        videodirection = request.POST.get('videodirection')
        videotype = request.POST.get('videotype')
        devicebrand = request.POST.get('devicebrand')
        devicetype = request.POST.get('devicetype')
        print devicestatus,devicegroup,deviceregion,videodirection,videotype,devicebrand,devicetype
        if devicestatus != 0:
            devicestatusf = AddDeviceStatusForm(request.POST)
            if devicestatusf.is_valid():
                result = DeviceStatus.objects.filter(name=devicestatus).count()
                if result == 0:
                    DeviceStatus.objects.create(name=devicestatus)
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicestatusstatus': '添加成功'})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicestatusstatus': '已存在'})

        elif devicegroup != 0:
            print 'elif'
            devicegroupf = AddDeviceGroupForm(request.POST)
            print devicegroupf
            if devicegroupf.is_valid():
                result = DeviceGroup.objects.filter(name=devicegroup).count()
                if result == 0:
                    DeviceGroup.objects.create(name=devicegroup)
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicegroupstatus': '添加成功'})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicegroupstatus': '已存在'})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid})
        elif deviceregion != 0:
            deviceregionf = AddDeviceRegionForm(request.POST)
            if deviceregionf.is_valid():
                result = DeviceRegion.objects.filter(name=deviceregion).count()
                if result == 0:
                    DeviceRegion.objects.create(name=deviceregion)
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'deviceregionstatus': '添加成功'})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'deviceregionstatus': '已存在'})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid})
        elif videodirection != 0:
            videodirectionf = AddVideoDirectionForm(request.POST)
            if videodirectionf.is_valid():
                result = VideoDirection.objects.filter(name=videodirection).count()
                if result == 0:
                    VideoDirection.objects.create(name=videodirection)
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'videodirectionstatus': '添加成功'})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'videodirectionstatus': '已存在'})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid})
        elif videotype != 0:
            videotypef = AddVideoTypeForm(request.POST)
            if videotypef.is_valid():
                result = VideoType.objects.filter(name=videotype).count()
                if result == 0:
                    VideoType.objects.create(name=videotype)
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'videotypestatus': '添加成功'})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'videotypestatus': '已存在'})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid})
        elif devicebrand != 0:
            devicebrandf = AddDeviceBrandForm(request.POST)
            if devicebrandf.is_valid():
                result = DeviceBrand.objects.filter(name=devicebrand).count()
                if result == 0:
                    DeviceBrand.objects.create(name=devicebrand)
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicebrandstatus': '添加成功'})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicebrandstatus': '已存在'})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid})
        elif devicetype != 0:
            devicetypef = AddDeviceTypeForm(request.POST)
            if devicetypef.is_valid():
                devicebrandid = request.POST.get('devicebrandid')
                result = DeviceType.objects.filter(name=devicetype,id=devicebrandid).count()
                if result == 0:
                    DeviceType.objects.create(brandid=devicebrandid,name=devicetype)
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicetypestatus': '添加成功'})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicetypestatus': '已存在'})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid})
    else:
        return render_to_response('AddBasicInfo.html',
                                  {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                   'deviceregionform': deviceregionform, 'videodirectionform': videodirectionform,
                                   'videotypeform': videotypeform, 'devicebrandform': devicebrandform,
                                   'devicetypeform': devicetypeform, 'devicebrandid': devicebrandid})




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



