from django.dispatch import Signal

# Custom signal with an additional argument for the request object
send_article_signal = Signal()