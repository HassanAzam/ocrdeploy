from django.shortcuts import render
from .forms import uploadform
import os
from PIL import Image
import pytesseract
from django.conf import settings

os.environ["TESSDATA_PREFIX"] = os.path.dirname(settings.BASE_DIR)+"/tessdata/"


def home(request):
    img = None
    if request.method == 'POST':
        form = uploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            new = str(request.FILES["image"])
            print(os.path.dirname(settings.BASE_DIR)+"/media/")
            filepath = os.path.dirname(settings.BASE_DIR)+"/media/"
            img=pytesseract.image_to_string(Image.open(filepath+new), lang="urd")
		
            img=img.encode('utf-8')
            img=img.decode('utf-8')
       
            return render(request, 'firstpage/index.html', {
                        'form': form,
                        'img': img
            })
            
    else:
        form = uploadform()
    
    return render(request, 'firstpage/index.html', {
                        'form': form,
                        'img': img
                })


'''def do_tess(request):
    if request.method == 'POST':
        form = uploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect(do_tess)
    else:
        form = uploadform()                
    os.chdir (r'E:/umam/media/media')
    for f in glob.glob('*.*'):
        f=f
    
    n,s,e=f.partition('.')
    prv=n+s+e
    Image.open(prv)
    new='aaa'+s+e
    os.rename(prv,new)
    
    #print(new)
    pytesseract.pytesseract.tesseract_cmd = (r'E:/umam/Urduocr/Tesseract-OCR/tesseract.exe')
    img=pytesseract.image_to_string(Image.open(r'E:/umam/media/media/'+new), lang='urd')
        #result=pytesseract.image_to_string(Image.open('hhh.JPG'), lang='urd')
        #print (img)
    os.remove('aaa'+s+e)   
    img=img.encode('utf-8')
    img=img.decode('utf-8')
    
    

    return render(request, 'firstpage/index.html', {
        'img': img,
        'form': form,
        })'''
    
            
    


