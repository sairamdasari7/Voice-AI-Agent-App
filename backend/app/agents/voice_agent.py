
from app.scheduling.scheduler import book_appointment

def handle_conversation(text):

    text = text.lower()

    if "appointment" in text:
        return book_appointment("Dr Sharma", "10:00")

    if "cancel" in text:
        return "Your appointment has been cancelled"

    return "How can I help you today?"
