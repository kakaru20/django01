from django.shortcuts import render
import datetime # 1. datetimeモジュールをインポート

def home_page_view(request):
    # 2. 現在の日時を取得
    now = datetime.datetime.now()
    
    # 3. テンプレートに渡すデータを作成（Pythonの辞書）
    context = {
        'current_time': now,
    }
    
    # 4. render関数の第3引数としてcontextを渡す
    return render(request, 'home.html', context)