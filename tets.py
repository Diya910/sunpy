import numpy as np

# Example function from differential_rotation.py (this is a placeholder)
def get_rotation_rate(latitude):
    """
    Placeholder function to calculate the solar rotation rate at a given latitude.
    This is just a basic example and should be replaced with the actual function from SunPy.
    """
    # Example of a simple linear differential rotation model (not accurate for SunPy, just a placeholder)
    if latitude > 90 or latitude < -90:
        raise ValueError("Latitude must be between -90 and 90 degrees.")
    equator_rate = 2.0  # Rotation rate at the equator in radians/day
    pole_rate = 1.0     # Rotation rate at the poles in radians/day
    return equator_rate - (equator_rate - pole_rate) * (latitude / 90)

# Function to test edge cases
def test_differential_rotation():
    # Test latitudes at extreme ends and at equator
    latitudes = [-90, -60, -30, 0, 30, 60, 90]
    for lat in latitudes:
        try:
            rate = get_rotation_rate(lat)
            print(f"Latitude: {lat} degrees -> Rotation Rate: {rate} rad/day")
        except ValueError as e:
            print(f"Error for Latitude {lat}: {e}")

# Run the test
test_differential_rotation()
