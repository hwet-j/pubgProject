from django import forms
from pro.models import MatchData, PgcList


class MatchForm(forms.ModelForm):
    class Meta:
        model = PgcList  # 사용할 모델
        fields = ['create_date', 'tournament_type', 'create_date']
        labels = {
            'match_id': '매치 아이디',
            'tournament_type': '대회 종류',
            'create_date': '게임 생성시간',
        }
