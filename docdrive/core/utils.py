from django.conf import settings
import os, math


class Utils:

    @staticmethod
    def user_media_directory(request, user):        
        directory = os.path.join(settings.MEDIA_ROOT, user.storage)        
        size = 0

        for path, dirs, files in os.walk(directory):
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)
        
        return (directory, Utils.file_size(size))
    
    @staticmethod
    def file_extension(filename):
        return os.path.splitext(filename)[1]      

    @staticmethod
    def file_size(bytes, suffix='B'):        
        if bytes > 0:
            m = int(math.floor(math.log(bytes, 1024)))
            v = bytes / math.pow(1024, m)
            if m > 7:
                return '{:-1f}{}{}'.format(v, 'Yi', suffix)
            return '{:3.1f}{}{}'.format(v, ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z'][m], suffix)
        return '0 Bites'
