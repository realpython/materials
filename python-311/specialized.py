import dis


def header(text):
    print("\n", f" {text} ".center(79, "="))


def feet_to_meters(feet):
    return 0.3048 * feet


header("Before any invocation")
dis.dis(feet_to_meters)

feet_to_meters(1.1)
feet_to_meters(2.2)
feet_to_meters(3.3)
feet_to_meters(4.4)
feet_to_meters(5.5)
feet_to_meters(6.6)
feet_to_meters(7.7)
header("After 7 float invocations")
dis.dis(feet_to_meters, adaptive=True)

feet_to_meters(8.8)
header("After 8 float invocations")
dis.dis(feet_to_meters, adaptive=True)

for feet in range(52):
    feet_to_meters(feet)
header("After 8 float and 52 int invocations")
dis.dis(feet_to_meters, adaptive=True)

feet_to_meters(52)
header("After 8 float and 53 int invocations")
dis.dis(feet_to_meters, adaptive=True)
