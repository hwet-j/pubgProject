from django import forms
from gamer.models import Matchdata, Matchlist


class MatchForm(forms.ModelForm):
    class Meta:
        model = Matchlist  # 사용할 모델
        fields = ['user_name', 'create_date', 'match_id']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'user_name': '아이디',
            'create_date': '게임 생성시간',
            'match_id': '매치 아이디',
        }
