project=mysite
env=env/bin/activate

test:
	 cd $(project) && python manage.py test
