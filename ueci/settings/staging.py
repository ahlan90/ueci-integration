from .base import *
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://qvewcathrylzlg:4abc2bb3f7b599611b6c21df65026845d5e3ec267433f1143f93014e4bd094c2@ec2-54-161-208-31.compute-1.amazonaws.com:5432/d7smqlghoanvaj'
    )
}