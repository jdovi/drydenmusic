from django.conf import settings
from django.template import Context
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from drydenmusic.settings import EMAIL_PROVIDER
from DrydenMusicApp.management.commands import SendEmail_Base

#python manage.py   SendEmail     content_id
#                 (mgt command)   (various)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('content_id')

    def handle(self, *args, **options):
        
        #capture content_id which will indicate which piece of functionality we're after
        content_id = options['content_id']       
        
        EMAIL_PROVIDER = 'sendgrid'
        to = 'jessedovi@gmail.com'
        subject = 'testing email system'
        context = {}
        html_body = render_to_string('mail/new_upload_renderer.html', context)
        
        #construct email and send
        SendEmail_Base.Send(to,
                            subject,
                            html_body,
                            EMAIL_PROVIDER)

