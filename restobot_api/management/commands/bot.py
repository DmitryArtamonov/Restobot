from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        from telegram_bot.bot_handler import start_bot
        self.stdout.write(self.style.SUCCESS('Command executed successfully'))
        start_bot()
