from pytube import YouTube
from moviepy.editor import *
import os

def download_video(url, quality='highest'):
    try:
        # إنشاء كائن YouTube
        yt = YouTube(url)
        
        # الحصول على جميع الجودات المتاحة
        streams = yt.streams.filter(progressive=True)
        
        if quality == 'highest':
            # تحميل أعلى جودة متاحة
            video = streams.get_highest_resolution()
        elif quality == 'lowest':
            # تحميل أقل جودة متاحة 
            video = streams.get_lowest_resolution()
        else:
            # تحميل جودة محددة
            video = streams.filter(res=quality).first()
            
        # تحميل الفيديو
        print(f"جاري تحميل: {yt.title}")
        video.download()
        print("تم التحميل بنجاح!")
        
    except Exception as e:
        print(f"حدث خطأ: {str(e)}")

# مثال على الاستخدام
url = input("أدخل رابط الفيديو: ")
print("\nاختر الجودة المطلوبة:")
print("1. أعلى جودة")
print("2. أقل جودة") 
print("3. 720p")
print("4. 480p")
print("5. 360p")

choice = input("اختيارك (1-5): ")

quality_options = {
    '1': 'highest',
    '2': 'lowest',
    '3': '720p',
    '4': '480p',
    '5': '360p'
}

if choice in quality_options:
    download_video(url, quality_options[choice])
else:
    print("اختيار غير صالح!")
