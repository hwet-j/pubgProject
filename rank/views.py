from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator     # 페이징을 위한 라이브러리
import csv

''' 페이지의 첫 화면 '''
def index(request):
    # # page = request.GET.get('page', '1')  # 페이지
    # # match_list = PgcList.objects.order_by('-create_date')     # 앞에 - 가 붙으면 내림 차순
    # # paginator = Paginator(match_list, 20)  # 페이지당 20개 씩 보여주기
    # # page_obj = paginator.get_page(page)
    # # context = {'PgcList' : page_obj}
    # return render(request, 'pro/home.html', context)
    return render(request, "rank/rank_home.html")