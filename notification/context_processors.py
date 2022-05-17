from notification.models import Notification

def notification(request):
    new_notifications = Notification.objects.filter(seen = False).count()
    params = {
        'notify': new_notifications,
    }
    return params