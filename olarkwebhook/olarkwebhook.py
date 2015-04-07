import webapp2
import cgi

from google.appengine.api import mail
from django.utils import simplejson as json

# Change these email addresses
DEFAULT_EMAIL = 'benc@olark.com'
GROUP_TO_EMAIL = {'Sales': 'benc@olark.com'}


class MainPage(webapp2.RequestHandler):
    def post(self):
        if self.request.body:
            conversation = json.loads(self.request.body)

            is_offline_message = (conversation['items'][0]['kind'] == 'OfflineMessage')

            if is_offline_message:
                groups = conversation.get('groups', None)
                if groups:
                    group = conversation['groups'][0]
                else:
                    group = None

                destination_email = GROUP_TO_EMAIL.get(group, DEFAULT_EMAIL)
                # attempt to lookup group to email address mapping

                self._format_and_send_offline_message(
                    to=destination_email,
                    conversation=conversation)

            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write(conversation)
            self.response.write('true')
        else:
            self.response.write('false')

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('false')


    def _format_and_send_offline_message(self, to, conversation):
        sender = "%s <%s>" % (conversation['visitor']['fullName'], conversation['visitor']['emailAddress'])
        subject = "Offline Email Message"

        message_body = conversation['items'][0]['body']

        body = """
Offline Message from page:

%s
        """ % (message_body)

        print to
        print sender
        print body

        mail.send_mail(sender=sender,
                  to=to,
                  subject=subject,
                  body=body)


# Start app
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
