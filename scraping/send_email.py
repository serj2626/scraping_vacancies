from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
from scraping_service.settings import EMAIL_HOST_USER


User = get_user_model()


# subject, from_email, to = "hello", "from@example.com", "to@example.com"
# text_content = "This is an important message."
# html_content = "<p>This is an <strong>important</strong> message.</p>"
# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
# msg.attach_alternative(html_content, "text/html")
# msg.send()
