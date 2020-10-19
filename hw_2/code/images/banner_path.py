import os


class BannerPath:
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    IMAGE_PATH = os.path.join(BASEDIR, 'banner.jpg')
