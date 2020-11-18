# Converting time from 12h to 24h


def time_conversion(s):
    for i in range(len(s)):
        if s[-2:] == 'PM':
            if s[:2] != '12':
                re = s[:2]
                res = int(re) + 12
                result = str(res) + s[2:-2]
                return str(result)
        elif s[-2:] != 'PM':
            if s[:2] == '12':
                re = s[:2]
                res = int(re) - 12
                result = str(res) + '0' + s[2:-2]
                return str(result)

    return str(s[:-2])


s_time = '12:01:12PM'
print(time_conversion(s_time))
