import re


def _is_br_number(tel):
    if tel[0] == '+':
        return tel[:3] == '+55'
    return True


def remove_country_code(tel):
    if tel[:3] == "+55":
        tel = tel[3:]

    return tel


def get_string_number(tel):
    return ''.join(re.findall(r'\d', tel))


def parse_phone_numbe(tel):
    country_code = "+55"
    sp_ddd = "11"

    if not _is_br_number(tel):
        return "+" + get_string_number(tel)

    tel = remove_country_code(tel)
    tel = get_string_number(tel)

    if tel[0] == "9":
        tel = country_code + sp_ddd + tel

    elif "0" in tel[0]:
        tel = country_code + tel[1:]

    elif "11" in tel[0:2]:
        tel = country_code + tel

    else:
        tel = country_code + sp_ddd + tel

    if len(tel) > 14:
        raise Exception(
            "Número com mais caracteres do que o permitido: %s" % tel)

    return tel


if __name__ == "__main__":
    phones = ["985182851", "85182851", "11985182851", "985182851", "1185182851", "01185182851", "8518285", "9851828511",
              "+5511985182851", "+551185182851", "011985182851", "01185182851", "98518-2851", "8518-2851", "(11)985182851", "(11)98518-2851"]
    for phone in phones:
        try:
            print("%s ---> %s" % (phone, parse_phone_numbe(phone)))
        except Exception as e:
            print(e)
