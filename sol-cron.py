from astral import LocationInfo
from astral.sun import sun, azimuth as get_az, elevation as get_al
import datetime

city = LocationInfo("Bengaluru", "India", "Asia/Kolkata", 13.0545, 77.6921)

s = sun(city.observer, date=datetime.date.today())

now = datetime.datetime.now(datetime.timezone.utc)

curr_azimuth = get_az(city.observer, now)
curr_altitude = get_al(city.observer, now)

x = (curr_azimuth/360) * 600
y = 350 - (curr_altitude/90) * 300

with open("template.svg", "r") as f:
    lines = f.readlines()

date_str = datetime.date.today().strftime("%b %d")
new_point = f'  <circle cx="{x: .2f}" cy="{y: .2f}" r="2" fill="#fbbf24">\n'
new_point+= f' <title>{date_str}: {curr_altitude:.1f}deg alt</title>\n'
new_point+= f'</circle>\n'

for i, line in enumerate(lines):
    if"</g>" in line:
        lines.insert(i, new_point)
        break

with open("template.svg", "w") as f:
    f.writelines(lines)