import psutil

battery = psutil.sensors_battery()

if battery is not None:
    plugged = battery.power_plugged
    percent = battery.percent

    if percent <= 30 and not plugged:
        print("Battery is low. Please plug in your charger.")

        from pynotifier import Notification

        Notification(
            title="Battery Low!!",
            description="Battery is low. Please plug in your charger.",
            duration=5,  # Duration in seconds
            urgency="normal"
        ).send()
else:
    print("Battery information is not available on this system.")
