from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import magic
import re
import chardet
import codecs
import ass
import os
from POST.models import *


def AssWeTran(SourceFileName):
    SourceFile = open(SourceFileName, 'rb')
    FileEnco = chardet.detect(SourceFile.read()).get('encoding')
    SourceFile.close()
    # 按文件编码重新打开文件
    SourceFile = codecs.open(SourceFileName, 'rb', FileEnco)
    TargetFile = codecs.open(SourceFileName + '.srt', 'w', 'utf-8')

    AssFile = ass.parse(SourceFile)
    TimeDic = dict()

    for event in AssFile.events:
        if not re.match('//', event.text) and not event.text == '':
            StartTime = str(event.start)
            EndTime = str(event.end)
            StartTime = '0' + StartTime
            StartTime = StartTime[:-3]
            StartTime = re.sub(r'\.', ',', StartTime)
            EndTime = '0' + EndTime
            EndTime = EndTime[:-3]
            EndTime = re.sub(r'\.', ',', EndTime)
            Time = StartTime + ' --> ' + EndTime
            SubTitle = re.sub(r'{[^}]*}', '', event.text)
            SubTitle = re.sub(r'\\N', '\n', SubTitle)
            if not Time in TimeDic.keys():
                TimeDic[Time] = SubTitle
            else:
                TimeDic[Time] = TimeDic[Time] + '\n' + SubTitle

    i = 1

    for key, value in TimeDic.items():
        TargetFile.write(str(i))
        TargetFile.write('\n')
        TargetFile.write(key)
        TargetFile.write('\n')
        TargetFile.write(value)
        TargetFile.write('\n')
        TargetFile.write('\n')
        i = i + 1
    TargetFile.close()
    return TargetFile.name


def simple_upload(request):
    tag_list = Article.tags.all()
    message_list = Message.objects.order_by('-publish_time')[:3]
    context = {'tag_list': tag_list, 'message_list': message_list}
    if request.method == 'POST' and request.FILES['myfile']:
        if request.FILES['myfile'].size > 500000:
            return render(request, 'AssWeTran.html',
                          {'notification': '上传的文件大小不能超过500k！！'})
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        SourceFileName = fs.path(filename)
        TargetFile = AssWeTran(SourceFileName)

        with open(TargetFile, 'rb') as fh:

            response = HttpResponse(fh.read(),
                                    content_type="application/text/plain")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(TargetFile)
            response[
                'Content-Disposition'] = 'attachment;filename="AssWeTran.srt"'
            return response
    return render(request, 'AssWeTran.html', context)
