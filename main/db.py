def sqlite(base_dir):
    return  {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': base_dir / 'db.sqlite3',
    }

def postgresql():
    return {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "stores",
        "USER": "postgres",
        "PASSWORD": "2004Leonel.",
        "HOST": "localhost",
        "PORT": "5432",
    }