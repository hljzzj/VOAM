# coding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from website.forms import AddVideoDeviceForm,AddDeviceStatusForm,AddDeviceGroupForm,AddDeviceRegionForm,AddVideoDirectionForm,AddVideoTypeForm,AddDeviceBrandForm,AddDeviceTypeForm
from website.models import DeviceStatus,DeviceGroup,DeviceRegion,VideoDirection,VideoType,DeviceBrand,DeviceType,ServerHostDevice,VideoDevice,NVRDevice,NetworkDevice


def Index(request):
    good_serverlist = VideoDevice.objects.all()
    return render_to_response('index.html')


def AddBasicInfo(request):
    devicestatusform = AddDeviceStatusForm()
    devicegroupform = AddDeviceGroupForm()
    deviceregionform = AddDeviceRegionForm()
    videodirectionform = AddVideoDirectionForm()
    videotypeform = AddVideoTypeForm()
    devicebrandform = AddDeviceBrandForm()
    devicetypeform = AddDeviceTypeForm()
    devicebrandid = DeviceBrand.objects.all()
    devicestatus_list = DeviceStatus.objects.all()
    devicegroup_list = DeviceGroup.objects.all()
    deviceregion_list = DeviceRegion.objects.all()
    videodirection_list = VideoDirection.objects.all()
    videotype_list = VideoType.objects.all()
    devicebrand_list = DeviceBrand.objects.all()
    devicetype_list = DeviceType.objects.all()
    if request.method == 'POST':
        devicestatus = request.POST.get('devicestatus')
        devicegroup = request.POST.get('devicegroup')
        deviceregion = request.POST.get('deviceregion')
        videodirection = request.POST.get('videodirection')
        videotype = request.POST.get('videotype')
        devicebrand = request.POST.get('devicebrand')
        devicetype = request.POST.get('devicetype')
        print devicestatus,devicegroup,deviceregion,videodirection,videotype,devicebrand,devicetype
        if devicestatus != None:
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
                                               'devicebrandid': devicebrandid, 'devicestatusstatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicestatusstatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                temp = devicestatusf.errors.as_data()
                print temp

        elif devicegroup != None:
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
                                               'devicebrandid': devicebrandid, 'devicegroupstatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicegroupstatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
        elif deviceregion != None:
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
                                               'devicebrandid': devicebrandid, 'deviceregionstatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'deviceregionstatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
        elif videodirection != None:
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
                                               'devicebrandid': devicebrandid, 'videodirectionstatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'videodirectionstatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
        elif videotype != None:
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
                                               'devicebrandid': devicebrandid, 'videotypestatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'videotypestatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
        elif devicebrand != None:
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
                                               'devicebrandid': devicebrandid, 'devicebrandstatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicebrandstatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
        elif devicetype != None:
            devicetypef = AddDeviceTypeForm(request.POST)
            if devicetypef.is_valid():
                devicebrand_id = request.POST.get('devicebrandid')
                devicetype = request.POST.get('devicetype')
                result = DeviceType.objects.filter(name=devicetype,brandid_id=devicebrand_id).count()
                if result == 0:
                    DeviceType.objects.create(brandid_id=devicebrand_id,name=devicetype)
                    #devicebrandid = DeviceBrand.objects.all()
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicetypestatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicetypestatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'videodirectionform': videodirectionform, 'videotypeform': videotypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})

    return render_to_response('AddBasicInfo.html',
                                  {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                   'deviceregionform': deviceregionform, 'videodirectionform': videodirectionform,
                                   'videotypeform': videotypeform, 'devicebrandform': devicebrandform,
                                   'devicetypeform': devicetypeform, 'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'videodirectionlist': videodirection_list,
                                               'videotypelist': videotype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})




def AddVideoDevice(request):
    addvideodevice = AddVideoDeviceForm()
    group_item = DeviceGroup.objects.all()
    devicebrand_item = DeviceBrand.objects.all()
    devicetype_item = DeviceType.objects.all()
    deviceregion_item = DeviceRegion.objects.all()
    videotype_item = VideoType.objects.all()
    videodirection_item = VideoDirection.objects.all()
    videodeivce_list = VideoDevice.objects.all()

    if request.method == 'POST':
        form = AddVideoDeviceForm(request.POST)
        print form
        if form.is_valid():
            pid = request.POST.get('pid',None)
            name = request.POST.get('name')
            group = request.POST.get('group')
            region = request.POST.get('region')
            direction = request.POST.get('direction')
            vtype = request.POST.get('vtype')
            ip = request.POST.get('ip')
            brand =request.POST.get('brand')
            dtype = request.POST.get('dtype')
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            gpslon = request.POST.get('gpslon',None)
            gpswei = request.POST.get('gpswei',None)
            print pid,name,group,region,direction,vtype,ip,username,password,gpslon,gpswei,brand,dtype
            result = VideoDevice.objects.filter(ip=ip).count()
            result1 = VideoDevice.objects.filter(pid=pid).count()
            if result == 0 and result1 == 0:
                VideoDevice.objects.create(pid=pid,name=name,groupid_id=group,regionid_id=region,directionid_id=direction,vtypeid_id=vtype,ip=ip,username=username,password=password,gpslon=gpslon,gpswei=gpswei,brandid_id=brand,dtypeid_id=dtype)
                return render_to_response('AddVideoDevice.html',{'form':addvideodevice,'grouplist':group_item,'devicebrand_item':devicebrand_item,'devicetype_item':devicetype_item,'deviceregion_item':deviceregion_item,'videotype_item':videotype_item,'videotype_item':videotype_item,'videodirection_item':videodirection_item,'videodevice_list':videodeivce_list,'addstatus':'添加成功'})
            elif result != 0:
                return render_to_response('AddVideoDevice.html', {'form': addvideodevice,'grouplist':group_item,'devicebrand_item':devicebrand_item,'devicetype_item':devicetype_item,'deviceregion_item':deviceregion_item,'videotype_item':videotype_item,'videotype_item':videotype_item,'videodirection_item':videodirection_item,'videodevice_list':videodeivce_list, 'addstatus': 'IP已存在'})
            else:
                return render_to_response('AddVideoDevice.html',{'form':addvideodevice,'grouplist':group_item,'devicebrand_item':devicebrand_item,'devicetype_item':devicetype_item,'deviceregion_item':deviceregion_item,'videotype_item':videotype_item,'videotype_item':videotype_item,'videodirection_item':videodirection_item,'videodevice_list':videodeivce_list,'addstatus':'ID已存在'})
        else:
            return render_to_response('AddVideoDevice.html', {'form': addvideodevice,'grouplist':group_item,'devicebrand_item':devicebrand_item,'devicetype_item':devicetype_item,'deviceregion_item':deviceregion_item,'videotype_item':videotype_item,'videotype_item':videotype_item,'videodirection_item':videodirection_item,'videodevice_list':videodeivce_list})
    else:
        return render_to_response('AddVideoDevice.html', {'form': addvideodevice,'grouplist':group_item,'devicebrand_item':devicebrand_item,'devicetype_item':devicetype_item,'deviceregion_item':deviceregion_item,'videotype_item':videotype_item,'videotype_item':videotype_item,'videodirection_item':videodirection_item,'videodevice_list':videodeivce_list})

def UpdateVideoDevice(request,videoID):
    updatevideodevice = UpdateVideoDeviceForm()
    group_item = DeviceGroup.objects.all()
    devicebrand_item = DeviceBrand.objects.all()
    devicetype_item = DeviceType.objects.all()
    deviceregion_item = DeviceRegion.objects.all()
    videotype_item = VideoType.objects.all()
    videodirection_item = VideoDirection.objects.all()
    videodeivce_list = VideoDevice.objects.all()
    if request.method == 'POST':
        form = AddVideoDeviceForm(request.POST)
        print form
        if form.is_valid():
            pid = request.POST.get('pid', None)
            name = request.POST.get('name')
            group = request.POST.get('group')
            region = request.POST.get('region')
            direction = request.POST.get('direction')
            vtype = request.POST.get('vtype')
            ip = request.POST.get('ip')
            brand = request.POST.get('brand')
            dtype = request.POST.get('dtype')
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            gpslon = request.POST.get('gpslon', None)
            gpswei = request.POST.get('gpswei', None)
            print pid, name, group, region, direction, vtype, ip, username, password, gpslon, gpswei, brand, dtype
            result = VideoDevice.objects.filter(ip=ip).count()
            result1 = VideoDevice.objects.filter(pid=pid).count()
            if result == 0 and result1 == 0:
                VideoDevice.objects.update(pid=pid, name=name, groupid_id=group, regionid_id=region,
                                           directionid_id=direction, vtypeid_id=vtype, ip=ip, username=username,
                                           password=password, gpslon=gpslon, gpswei=gpswei, brandid_id=brand,
                                           dtypeid_id=dtype)
                return render_to_response('AddVideoDevice.html', {'form': addvideodevice, 'grouplist': group_item,
                                                                  'devicebrand_item': devicebrand_item,
                                                                  'devicetype_item': devicetype_item,
                                                                  'deviceregion_item': deviceregion_item,
                                                                  'videotype_item': videotype_item,
                                                                  'videotype_item': videotype_item,
                                                                  'videodirection_item': videodirection_item,
                                                                  'videodevice_list': videodeivce_list,
                                                                  'addstatus': '添加成功'})
            elif result != 0:
                return render_to_response('AddVideoDevice.html', {'form': up, 'grouplist': group_item,
                                                                  'devicebrand_item': devicebrand_item,
                                                                  'devicetype_item': devicetype_item,
                                                                  'deviceregion_item': deviceregion_item,
                                                                  'videotype_item': videotype_item,
                                                                  'videotype_item': videotype_item,
                                                                  'videodirection_item': videodirection_item,
                                                                  'videodevice_list': videodeivce_list,
                                                                  'addstatus': 'IP已存在'})
            else:
                return render_to_response('AddVideoDevice.html', {'form': addvideodevice, 'grouplist': group_item,
                                                                  'devicebrand_item': devicebrand_item,
                                                                  'devicetype_item': devicetype_item,
                                                                  'deviceregion_item': deviceregion_item,
                                                                  'videotype_item': videotype_item,
                                                                  'videotype_item': videotype_item,
                                                                  'videodirection_item': videodirection_item,
                                                                  'videodevice_list': videodeivce_list,
                                                                  'addstatus': 'ID已存在'})
        else:
            return render_to_response('AddVideoDevice.html', {'form': addvideodevice, 'grouplist': group_item,
                                                              'devicebrand_item': devicebrand_item,
                                                              'devicetype_item': devicetype_item,
                                                              'deviceregion_item': deviceregion_item,
                                                              'videotype_item': videotype_item,
                                                              'videotype_item': videotype_item,
                                                              'videodirection_item': videodirection_item,
                                                              'videodevice_list': videodeivce_list})
    else:
        return render_to_response('AddVideoDevice.html', {'form': addvideodevice, 'grouplist': group_item,
                                                          'devicebrand_item': devicebrand_item,
                                                          'devicetype_item': devicetype_item,
                                                          'deviceregion_item': deviceregion_item,
                                                          'videotype_item': videotype_item,
                                                          'videotype_item': videotype_item,
                                                          'videodirection_item': videodirection_item,
                                                          'videodevice_list': videodeivce_list})


