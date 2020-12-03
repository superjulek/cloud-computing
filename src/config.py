"""Config file, default values, can be overwritten, all in SI system"""

class constants:
    """Class containting material constants"""

    lambda_val = 380  # thermal conductivity
    density_val = 9000  # material density
    specific_heat_val = 380  # specific heat capacity
    length_val = 1

class initials:
    """Initial temps"""

    temp_left = 300
    temp_right = 900

class stepping:
    """Time and distance deltas"""

    time_delta = 1
    space_delta = 0.05

class simulation:
    """Simulation config"""

    max_step_num = 1000
    expected_diff = 100  # Expected temperature difference between ends
    run_check = False  # Whether to run check calculation with more accurate mesh