from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='w$xjx_u7a*n16x3r+b)76m2f&1$^dk)#6dw3u5!p!wfg&uvuqj')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
