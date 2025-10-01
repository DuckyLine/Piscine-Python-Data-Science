from datetime import datetime

dt = datetime.now()

print(f"Seconds since January 1, 1970: {f'{datetime.timestamp(dt):,}'} or {f'{datetime.timestamp(dt):.2e}'} in scientific notation\n\
{dt.strftime('%b')} {dt.day} {dt.year}")
