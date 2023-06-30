This is an educational project.

Local Deployment:
>> clone the project
>> create a virtual environment and activate it
>> install requirements (pip install -r requirements.txt)
>> run the following two commands
>> python manage.py makemigrations
>> python manage.py migrate


regex for converting src and href link to static:
search:
\b(src|href)="([^"]*)"\b

change:
$1="{% static '$2' %}"