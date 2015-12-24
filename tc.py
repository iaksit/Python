from random import randint


def generate_tc_no():
    tc_no = str(randint(100000000, 1000000000))
    lst_tc_no = list(map(int, tc_no))
    tc_no_checksum_first_digit = (sum(lst_tc_no[::2]) * 7 - sum(lst_tc_no[1::2])) % 10
    tc_no_checksum_last_digit = (sum(lst_tc_no[::]) + tc_no_checksum_first_digit) % 10
    return tc_no + str(tc_no_checksum_first_digit) + str(tc_no_checksum_last_digit)


print(generate_tc_no())
