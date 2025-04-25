def create_client_notification(client, action="enrolled"):
    """Create a notification for client actions"""
    from .models import Notification
    
    message = f"New client {action}: {client.full_name}"
    
    # Create notification for all staff (you might want to refine this)
    Notification.objects.create(
        message=message,
        related_client=client
    )

def create_program_notification(program, action="updated"):
    """Create a notification for program actions"""
    from .models import Notification
    
    message = f"Health program {action}: {program.name}"
    
    # Create notification for all staff (you might want to refine this)
    Notification.objects.create(
        message=message,
        related_program=program
    )