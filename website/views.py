# coding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from website.forms import AddCameraDeviceForm,AddDeviceStatusForm,AddDeviceGroupForm,AddDeviceRegionForm,\
    AddCameraDirectionForm,AddCameraTypeForm,AddDeviceBrandForm,AddDeviceTypeForm,UpdateCameraDeviceForm
from website.models import DeviceStatus,DeviceGroup,DeviceRegion,CameraDirection,CameraType,DeviceBrand,\
    DeviceType,ServerHostDevice,CameraDevice,NVRDevice,NetworkDevice,Telecom

from django.db.models import Q

def Index(request):
    good_serverlist = CameraDevice.objects.all()
    return render_to_response('index.html')

def AddBasicInfo(request):
    devicestatusform = AddDeviceStatusForm()
    devicegroupform = AddDeviceGroupForm()
    deviceregionform = AddDeviceRegionForm()
    cameradirectionform = AddCameraDirectionForm()
    cameratypeform = AddCameraTypeForm()
    devicebrandform = AddDeviceBrandForm()
    devicetypeform = AddDeviceTypeForm()
    devicebrandid = DeviceBrand.objects.all()
    devicestatus_list = DeviceStatus.objects.all()
    devicegroup_list = DeviceGroup.objects.all()
    deviceregion_list = DeviceRegion.objects.all()
    cameradirection_list = CameraDirection.objects.all()
    cameratype_list = CameraType.objects.all()
    devicebrand_list = DeviceBrand.objects.all()
    devicetype_list = DeviceType.objects.all()
    if request.method == 'POST':
        devicestatus = request.POST.get('devicestatus')
        devicegroup = request.POST.get('devicegroup')
        deviceregion = request.POST.get('deviceregion')
        cameradirection = request.POST.get('cameradirection')
        cameratype = request.POST.get('cameratype')
        devicebrand = request.POST.get('devicebrand')
        devicetype = request.POST.get('devicetype')
        print devicestatus,devicegroup,deviceregion,cameradirection,cameratype,devicebrand,devicetype
        if devicestatus != None:
            devicestatusf = AddDeviceStatusForm(request.POST)
            if devicestatusf.is_valid():
                result = DeviceStatus.objects.filter(name=devicestatus).count()
                if result == 0:
                    DeviceStatus.objects.create(name=devicestatus)
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicestatusstatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicestatusstatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
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
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicegroupstatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicegroupstatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
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
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'deviceregionstatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'deviceregionstatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
        elif cameradirection != None:
            cameradirectionf = AddCameraDirectionForm(request.POST)
            if cameradirectionf.is_valid():
                result = CameraDirection.objects.filter(name=cameradirection).count()
                if result == 0:
                    CameraDirection.objects.create(name=cameradirection)
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'cameradirectionstatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'cameradirectionstatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
        elif cameratype != None:
            cameratypef = AddCameraTypeForm(request.POST)
            if cameratypef.is_valid():
                result = CameraType.objects.filter(name=cameratype).count()
                if result == 0:
                    CameraType.objects.create(name=cameratype)
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'cameratypestatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'cameratypestatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
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
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicebrandstatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicebrandstatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
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
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicetypestatus': '添加成功',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
                else:
                    return render_to_response('AddBasicInfo.html',
                                              {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                               'deviceregionform': deviceregionform,
                                               'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                               'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                               'devicebrandid': devicebrandid, 'devicetypestatus': '已存在',
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})
            else:
                return render_to_response('AddBasicInfo.html',
                                          {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                           'deviceregionform': deviceregionform,
                                           'cameradirectionform': cameradirectionform, 'cameratypeform': cameratypeform,
                                           'devicebrandform': devicebrandform, 'devicetypeform': devicetypeform,
                                           'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})

    return render_to_response('AddBasicInfo.html',
                                  {'devicestatusform': devicestatusform, 'devicegroupform': devicegroupform,
                                   'deviceregionform': deviceregionform, 'cameradirectionform': cameradirectionform,
                                   'cameratypeform': cameratypeform, 'devicebrandform': devicebrandform,
                                   'devicetypeform': devicetypeform, 'devicebrandid': devicebrandid,
                                               'devicestatuslist': devicestatus_list,
                                               'devicegrouplist': devicegroup_list,
                                               'deviceregionlist': deviceregion_list,
                                               'cameradirectionlist': cameradirection_list,
                                               'cameratypelist': cameratype_list, 'devicebrandlist': devicebrand_list,
                                               'devicetypelist': devicetype_list})


def UpdateCameraDevice(request,cameraID):
    group_item = DeviceGroup.objects.all()
    devicebrand_item = DeviceBrand.objects.all()
    devicetype_item = DeviceType.objects.all()
    deviceregion_item = DeviceRegion.objects.all()
    cameratype_item = CameraType.objects.all()
    cameradirection_item = CameraDirection.objects.all()
    cameradeivce_ID = CameraDevice.objects.filter(id=cameraID)
    form = UpdateCameraDeviceForm()
    #for item in cameradeivce_ID:
        #print item.name,item.pid
    if request.method == 'POST':
        form = UpdateCameraDeviceForm(request.POST)
        #print form
        if form.is_valid():
            pid = request.POST.get('pid', None)
            name = request.POST.get('name')
            group = request.POST.get('group')
            region = request.POST.get('region')
            direction = request.POST.get('direction')
            ctype = request.POST.get('ctype')
            ip = request.POST.get('ip')
            brand = request.POST.get('brand')
            dtype = request.POST.get('dtype')
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            gpslon = request.POST.get('gpslon', None)
            gpswei = request.POST.get('gpswei', None)
            result = CameraDevice.objects.filter(ip=ip).exclude(id=cameraID).count()  # 查找IP列相同与ID列不同的值有多少
            result1 = CameraDevice.objects.filter(pid=pid).exclude(id=cameraID).count()
            print 'ID:' + cameraID + ',' + 'pid:' + pid + ',' + 'name:' + name + ',' + 'group:' + group + ',' +\
                  'region:' + region + ',' + 'direction:' + direction + ',' + 'ctype:' + ctype + ',' + 'brand:' +\
                  brand + ',' + 'dtype:' + dtype + ',' + 'username:' + username + ',' + 'password:' + password +\
                  ',' + 'gpslon:' + gpslon + ',' + 'gpswei' + gpswei
            if result == 0 and result1 == 0:
                CameraDevice.objects.filter(id=cameraID).update(pid=pid,
                                                                name=name,
                                                                groupid_id=group,
                                                                regionid_id=region,
                                                                directionid_id=direction,
                                                                ctypeid_id=ctype,
                                                                ip=ip,
                                                                username=username,
                                                                password=password,
                                                                gpslon=gpslon,
                                                                gpswei=gpswei,
                                                                brandid_id=brand,
                                                                dtypeid_id=dtype)
                return render_to_response('UpdateDevice.html', {'cameradeivce_ID': cameradeivce_ID,'updatestatus': '修改成功'})
            elif result != 0:
                return render_to_response('UpdateDevice.html', {'cameradeivce_ID': cameradeivce_ID,'updatestatus': 'IP已存在'})
            else:
                return render_to_response('UpdateDevice.html', {'cameradeivce_ID': cameradeivce_ID,'updatestatus': 'ID已存在'})
        else:
            return render_to_response('UpdateDevice.html', {'cameradeivce_ID': cameradeivce_ID})
    else:
        edit_form = form
        return render_to_response('UpdateDevice.html', {'cameradevice_ID': cameradeivce_ID,'form':edit_form})


def DelCameraDevice(request,cameraID):
    CameraDevice.objects.filter(id=cameraID).delete()
    ok = CameraDevice.objects.filter(id=cameraID).count()
    if ok == 0:
        return render_to_response('Status.html',{'updatestatus':'删除成功'})
    else:
        return render_to_response('Status.html',{'updatestatus':'删除失败'})





def AddCameraDevice(request):
    addcameradevice = AddCameraDeviceForm()
    cameradevicelist = CameraDevice.objects.all()
    print cameradevicelist
    print addcameradevice
    if request.method == 'POST':
        form = AddCameraDeviceForm(request.POST)
        if form.is_valid():
            pid = request.POST.get('pid',None)
            name = request.POST.get('name')
            group = request.POST.get('group')
            region = request.POST.get('region')
            direction = request.POST.get('direction')
            ctype = request.POST.get('ctype')
            ip = request.POST.get('ip')
            brand =request.POST.get('brand')
            dtype = request.POST.get('dtype')
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            gpslon = request.POST.get('gpslon',None)
            gpswei = request.POST.get('gpswei',None)
            telecom = request.POST.get('telecom')
            nvrdevice = request.POST.get('nvrdevice')
            print pid,name,group,region,direction,ctype,ip,username,password,gpslon,gpswei,brand,dtype
            result = CameraDevice.objects.filter(ip=ip).count()
            result1 = CameraDevice.objects.filter(pid=pid).count()
            if result == 0 and result1 == 0:
                CameraDevice.objects.create(pid=pid,name=name,groupid_id=group,regionid_id=region,
                                           directionid_id=direction,ctypeid_id=ctype,ip=ip,username=username,
                                           password=password,gpslon=gpslon,gpswei=gpswei,brandid_id=brand,
                                           dtypeid_id=dtype,telecomid_id=telecom,nvrdeviceid_id=nvrdevice)
                return render_to_response('AddCameraDevice.html',{'form':addcameradevice,
                                                                  'cameradevice_list':cameradevicelist,
                                                                  'status':'添加成功'})
            elif result != 0:
                return render_to_response('AddCameraDevice.html', {'form': addcameradevice,
                                                                   'cameradevice_list':cameradevicelist,
                                                                   'status': 'IP已存在'})
            else:
                return render_to_response('AddCameraDevice.html',{'form':addcameradevice,
                                                                  'cameradevice_list':cameradevicelist,
                                                                  'status':'ID已存在'})
        else:
            return render_to_response('AddCameraDevice.html', {'form': addcameradevice,
                                                               'cameradevice_list':cameradevicelist})
    else:
        return render_to_response('AddCameraDevice.html', {'form': addcameradevice,
                                                           'cameradevice_list':cameradevicelist})
