from django.forms import inlineformset_factory

from .models import Album, Photo

# 폼셋이란 동일한 폼 여러 개로 구성된 폼을 말함
# 인라인 폼셋이란 메인 폼에 딸려 있는 하위 폼셋을 말하는 것으로, 테이블 간의 관계가 1:N 인 경우
# N 테이블의 레코드 여러 개를 한꺼번에 입력받기 위한 폼으로 사용된다.


# 1:N 관계인 Album, Photo 테이블을 이용해 사진 인라인 폼셋을 만듬
PhotoInlineFormSet = inlineformset_factory(Album, Photo,
                                           fields=['image', 'title', 'description'],
                                           extra=2)
