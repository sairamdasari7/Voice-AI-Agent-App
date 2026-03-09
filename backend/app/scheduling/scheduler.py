
appointments = []

doctors = {
    "Dr Sharma": ["10:00", "11:00", "14:00"],
    "Dr Ravi": ["09:00", "13:00", "16:00"]
}

def book_appointment(doctor, slot):

    if slot not in doctors[doctor]:
        return "Doctor not available at that time"

    for a in appointments:
        if a["doctor"] == doctor and a["slot"] == slot:
            return "Slot already booked"

    appointments.append({
        "doctor": doctor,
        "slot": slot
    })

    return f"Appointment booked with {doctor} at {slot}"

def list_appointments():
    return appointments
