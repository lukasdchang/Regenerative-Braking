# Variables
regen_torqueCMD = 0
speed_car = 0
speed_motor = 0
battery_voltage = 0
accelerator = 0
brake_pressure_front = 0
brake_pressure_rear = 0
k = 1  # You need to adjust this value accordingly
break_balance_distribution = 1  # You need to adjust this value accordingly

# Thresholds
speed_car_threshold = 5  # kph
speed_motor_threshold = 250  # RPM
brake_pressure_rear_threshold = 120  # PSI
brake_pressure_front_threshold = 120  # PSI
battery_voltage_maximum_threshold = 299  # V
accelerator_maximum_threshold = 0.05  # 5%
regen_torqueCMD_maximum = 100  # Nm

# State Variables
motor_controller_enable_state = False  # False indicates off/released
brake_shutoff_valve_state = False  # False indicates off/released
regen_feature_state = False  # False indicates off/released
HV_state = False  # False indicates off/released

# Regen Controller
if HV_state and regen_feature_state and motor_controller_enable_state and brake_pressure_rear < brake_pressure_rear_threshold:
    brake_shutoff_valve_state = True
else:
    brake_shutoff_valve_state = False

if brake_shutoff_valve_state and speed_car > speed_car_threshold and speed_motor > speed_motor_threshold \
        and accelerator < accelerator_maximum_threshold and battery_voltage < battery_voltage_maximum_threshold \
        and brake_pressure_front > brake_pressure_front_threshold:
    regen_torqueCMD = k * brake_pressure_front * ((1 / break_balance_distribution) - 1)
    if regen_torqueCMD > regen_torqueCMD_maximum:
        regen_torqueCMD = regen_torqueCMD_maximum
    else:
        regen_torqueCMD = 0
