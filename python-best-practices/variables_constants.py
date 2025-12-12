# Avoid this:
# hours = 35


# def compute_net_salary(hours):
#     return hours * 35 * (1 - (0.04 + 0.1))


# Favor this:
HOURLY_SALARY = 35
SOCIAL_SECURITY_TAX_RATE = 0.04
FEDERAL_TAX_RATE = 0.10

hours = 35


def compute_net_salary(hours):
    return hours * HOURLY_SALARY * \
        (1 - (SOCIAL_SECURITY_TAX_RATE + FEDERAL_TAX_RATE))
