from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    text_nospace = text.replace(' ','')
    total_len = len(text)
    total_len_nospace = len(text_nospace)
    word_count = len(text.split())
    return render(request, 'result.html', {
        'text' : text,
        'total_len' : total_len,
        'total_len_nospace' : total_len_nospace,
        'word_count' : word_count,
    })# html 로 data 보낼때 이렇게 dictionary 형식으로