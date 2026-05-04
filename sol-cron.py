from astral import LocationInfo
from astral.sun import sun, azimuth as get_az, elevation as get_al
import datetime

city = LocationInfo("Bengaluru", "India", "Asia/Kolkata", 13.0545, 77.6921)

now = datetime.datetime.now(datetime.timezone.utc)
curr_azimuth = get_az(city.observer, now)
curr_altitude = get_al(city.observer, now)

x = (curr_azimuth/360) * 600
y = 350 - (curr_altitude/90) * 300

now_ist = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
date_str = now_ist.strftime("%b %d, %Y | %I:%M %p IST")

with open("template.svg", "r") as f:
    lines = f.readlines()

new_point = f'  <circle cx="{x: .2f}" cy="{y: .2f}" r="2" fill="#fbbf24">\n'
new_point+= f' <title>{date_str}: {curr_altitude:.1f}deg alt</title>\n'
new_point+= f'</circle>\n'

updated_lines = []
for line in lines:
    if'id="last-update"' in line:
        updated_lines.append(f'  <text id="last-update" x="10" y="20" fill="#64748b" font-family="monospace">last update: {date_str}</text>\n')
    elif"</g>" in line:
        updated_lines.append(new_point)
        updated_lines.append(line)
    else:
        updated_lines.append(line)

with open("template.svg", "w") as f:
    f.writelines(updated_lines)




