from django.db.models.fields.files import ImageFieldFile, ImageField
from PIL import Image
import os


# 기존 이미지 파일명을 기준으로 썸네일 이미지 파일명을 만들어준다.
def _add_thumb(s):
    parts = s.split(".")
    parts.insert(-1, "thumb")
    # 이미지 확장자가 jpeg 또는 jpg 가 아니면 jpg로 변경
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)


# ImageFieldFile 상속받음, 파일 시스템에 직접 파일을 쓰고 지우는 작업을 함.
class ThumbnailImageFieldFile(ImageFieldFile):
    # 이미지를 처리하는 필드는 파일의 경로(path)와(url) 속성을 제공해야한다. 원본파일의 경로인 path
    # 속성에 추가해, 썸네일의 경로인 thumb_path 속성을 만들어 줌
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    # 원본 파일의 URL인 url 속성에 추가해 썸네일의 URL인 thumb_url속성을 만들어줌
    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    # 파일 시스템에 파일을 저장하고 생성하는 메소드
    def save(self, name, content, save=True):
        # 부모 ImageFieldFile 클래스의 save() 메소드를 호출해 원본 이미지를 저장
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)

        # 원본으로부터 128x128px 크기의 백그라운드 이미지를 만듬, 썸네일 이미지를 만드는 함수는 PIL 라이브러리
        # Image.thumbnail() 함수다, 이 함수는 썸네일을 만들 때 원본 이미지의 가로,세로 비율을 유지함
        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)
        # 가로,세로 비율이 동일한 128x128 크기의 백그라운드 이미지를만듬, 이미지의 색상은 흰색이고 완전 불투명한 이미지임
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        # "cannot write mode RGBA as JPEG"issue 해결하기!
        background = background.convert('RGB')
        # 썸네일과 백그라운드 이미지를 합쳐서 정사각형 모양의 썸네일 이미지를 만듬, 정사각형의 빈 공간은 백그라운드 이미지에 의해서 하얀색이 된다.
        background.paste(img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)))
        # 합쳐진 최종 이미지를 PNG 형식으로 파일 시스템의 thumb_path 경로에 저장
        background.save(self.thumb_path, 'PNG')

    # delete 호출시 원본 이미지 뿐만 아니라 썸네일 이미지도 같이 삭제 되도록한다.
    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)


# ThumbnailImageField 와 같은 새로운 FileField 클래스를 정의할 때는 그에 상응하는 File 처리 클래스를 attr_class 속성에
# 지정하는 것이 필수임, ThumbnailImageField 에 상응하는 File 클래스로 ThumbnailImageFieldFile을 지정함
class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    # 부모 ImageField 클래스의 생성자를 호출해 관련 속성들을 초기화
    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)