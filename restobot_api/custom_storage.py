from django.core.files.storage import FileSystemStorage

class CustomMediaStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None):
        location = location or 'media'
        super().__init__(location, base_url)