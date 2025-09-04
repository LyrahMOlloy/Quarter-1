# Motion Type Identifier Template
 
# Function 1: Convert velocity to m/s

def convert_velocity(value, unit):
    if unit == "ft/s":
        valv = value*0.3048
    elif unit == "km/s":
        valv = value*1000
    elif unit == "mi/s":
        valv = value*1609.34
    elif unit == "m/s":
        valv = value
    else:
        valv = "invalid unit"

    # TODO: Implement conversion using if-elif-else

    return valv

 

# Function 2: Convert acceleration to m/s²

def convert_acceleration(value, unit):
    if unit == "ft/s²":
        vala = value*0.3048
    elif unit == "km/s²":
        vala = value*1000
    elif unit == "mi/s²":
        vala = value*1609.34
    elif unit == "m/s²":
        vala = value
    else:
        vala = "invalid unit"

    """

    Convert acceleration to meters per second squared (m/s²)

    Supported units: m/s², ft/s², km/s², mi/s²

    """

    # TODO: Implement conversion using if-elif-else

    return vala

 
# Function 3: Determine motion type

def motion_type(v, a):
    if v > 0 and a == 0:
        mot_type = "Uniform Motion"
    elif v > 0 and a > 0:
        mot_type = "Accelerated Motion"
    elif v > 0 and a < 0:
        mot_type = "Decelerated Motion"
    elif v == 0:
        mot_type = "At Rest"
    else:
        mot_type = "Unable to determie motion type."



    # TODO: Implement selection structure to return motion type

    return mot_type

 

# --- Main Program ---

 

# Step 1: Input velocity

v_value = float(input("Enter velocity value: "))


v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

 

# Step 2: Input acceleration

a_value = float(input("Enter acceleration value: "))

a_unit = input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): ")

 

# Step 3: Convert to SI units

v_si = convert_velocity(v_value, v_unit)      # TODO: Call the conversion function

a_si = convert_acceleration(a_value, a_unit)  # TODO: Call the conversion function

 

# Step 4: Determine motion type

motion = motion_type(v_si, a_si)              # TODO: Call the motion type function

 

# Step 5: Display results

print("\n--- Results ---")

print(f"Velocity = {v_si:.3f} m/s")

print(f"Acceleration = {a_si:.3f} m/s²")

print(f"Motion Type = {motion}")

