from .notification_service import NotificationService

class ConsoleNotificationService(NotificationService):
    def notify(self, message: str):
        print(message)

