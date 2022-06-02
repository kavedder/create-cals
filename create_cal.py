# pip install python-dateutil
# replace `start` with your start date in the main section

from dateutil.parser import parse as dtparse
from dateutil.relativedelta import relativedelta


def dtfmt(dt):
    return dt.strftime('%Y%m%d')


def print_file(name, start_date, s):
    filename = f'{name.lower()}.{dtfmt(start_date)}.ical'
    print(filename)
    with open(filename, 'w') as outfi:
        outfi.write(s)


def create_cal(name, num_repeats, delta, emoji, start_date):
    s = f'''BEGIN:VCALENDAR
VERSION:2.0
X-WR-CALNAME:{name}
X-WR-TIMEZONE:America/Los_Angeles
CALSCALE:GREGORIAN

'''
    i = 1
    date = start_date
    while i <= num_repeats:
        date = date + delta
        title = f'{i} {emoji}'
        event = f'''BEGIN:VEVENT
DTSTART;VALUE=DATE:{dtfmt(date)}
DTEND;VALUE=DATE:{dtfmt(date)}
SUMMARY:{title}
X-GOOGLE-CALENDAR-CONTENT-TITLE:{title}
X-GOOGLE-CALENDAR-CONTENT-TYPE:text/html
END:VEVENT

'''
        s += event
        i += 1
    s += '''END:VCALENDAR'''
    return s


if __name__ == '__main__':
    start = dtparse('05/13/2022')
    day = relativedelta(days=1)
    week = relativedelta(days=7)
    month = relativedelta(months=1)

    day_emoji = '☀️'
    week_emoji = '⏳'
    month_emoji = '🗓️'

    for d in [('DAYS', 1000, day, day_emoji),
              ('WEEKS', 104, week, week_emoji),
              ('MONTHS', 24, month, month_emoji)]:
        s = create_cal(*d, start)
        print_file(d[0], d[1], s)
