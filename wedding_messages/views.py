from django.shortcuts import render
from .models import WeddingMessages

# Create your views here.

def mehndiMsgSubmit(request):

    if request.method == 'POST':
        newMessage = WeddingMessages(
            fromNames = request.POST['from-names'],
            message = request.POST['message'],
        )
        newMessage.save()

        return render(request, 'wedding_messages/thankyou.html')
    else:
        return render(request, 'wedding_messages/mehndiMsgSubmit.html')


def mehndiShowMsgs(request):
    queryset_list = WeddingMessages.objects.order_by('id') 
    print('query:')
    print (queryset_list)
    
    context = {'messages' : queryset_list}

    return render(request, 'wedding_messages/mehndiShowMsg.html', context)