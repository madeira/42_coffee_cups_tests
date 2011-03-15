project=mysite
env=env/bin/activate

test:
	. $(env) && cd $(project) && python manage.py test
