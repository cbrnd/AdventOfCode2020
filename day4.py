#-------------------------------------------------------------------------------
# Name:        module1
# Author:      brand
#-------------------------------------------------------------------------------

def main():

    print("valid: ", len(check()))
    print(data())

    pass


def data():

    passports = check()
    count = 0

    for passp in passports:

        passp = passp.split(' ')
        attributes = []
        for att in passp:

            att = att.split(':')
            if att[0] != '':
                attributes.append(att)

        if validate(attributes) == True:
            count += 1

    return count


def validate(atts):

    val = True

    for att in atts:

        c = att[0]
        d = att[1]

        if c == 'byr':
            if int(d) < 1920 or int(d) > 2002:
                val = False

        if c == 'iyr':
            if int(d) < 2010 or int(d) > 2020:
                val = False

        if c == 'eyr':
            if int(d) < 2020 or int(d) > 2030:
                val = False

        if c == 'hgt':
            if d.endswith(('cm', 'in')):
                suff = d[-2:]
                d = d[:len(d)-2]

                if suff == 'cm':
                    if int(d) < 150 or int(d) > 193:
                        val = False
                else:
                    if int(d) < 59 or int(d) > 76:
                        val = False
            else:
                val = False

        if c == 'hcl':
            if d[0] == '#' and len(d) == 7:
                if (d == r'^#[0-9a-fA-F]{6}$') == False:
                    val = False
            else:
                val = False

        if c == 'ecl':
            if (d == r'^(?:amb|blu|brn|gry|grn|hzl|oth)$') == False:
                val == False

        if c == 'pid':
            if len(d) == 9:
                for i in d:
                    if int(i) > 9 or int(i) < 0:
                        val = False
            else:
                val = False

        if c == 'cid':
            pass

    return val



def check():

    passports = read()
    args = 0
    valid = []
    str = ''

    for line in passports:

        if len(line) > 0 :
            args += line.count(':')
            str += line+' '

        else:

            if args == 8:
                valid.append(str)
            else:
                if args == 7:
                    if 'cid:' not in str:
                        valid.append(str)

            str = ''
            args = 0

    return valid


def read():

    passports = [str(line.strip('\n')) for line in open('input.txt', 'r')]

    return passports

if __name__ == '__main__':
    main()