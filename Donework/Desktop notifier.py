from plyer import notification

for i in range(0,1):
    title = 'TIME TO REST'
    message = 'You have used the computer too much. REST!'

    notification.notify(
    title=title,
    message=message,
    app_name='Desktop Notifier',
    timeout=20
    )
