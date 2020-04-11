"""
Requsítios:
 - A separação das duas últimas palabras deve ser `"and"` o resto deve ser `","`
 - Se receber um números negativo ou menor que zero retornar `"now"`
 - Deve ser divido em e nessa orderm`""year(s)", "hour(s)", minute(s)", "second(s)"`
 - númeross maior que 1 devem possuir a terminação no plural
 - Valores zerados não devem ser exbidos como por exemplo `"1 minute and 0 seconds" -> "1 minute"`

Resolução -> Dividir pelo maior valor pegar o restante e dividir pelo pŕoximo assim sucessivamente 

dict = {
    "year": x,
    "day": x,
    "hour": x,
    "minute": x,
    "second": x
}

Tabela:
1 min - > 60s
1 h - 3600s
1 day -> 86400s
1 year -> 31536000
"""

OPERATOR_IN_SECODS = {
    "year": 31536000,
    "day": 86400,
    "hour": 3600,
    "minute": 60,
    "second": 1
}


def convert(seconds, operator):
    many_time = seconds // OPERATOR_IN_SECODS[operator]
    left_time = seconds % OPERATOR_IN_SECODS[operator]

    return many_time, left_time


def generate_message(time, operator):
    if not time:
        return False
    terminator = "" if time == 1 else "s"
    return str(time) + " " + operator + terminator


def format_duration(seconds):
    if seconds == 0:
        return "now"

    time_dict = {
        "year": 0,
        "day": 0,
        "hour": 0,
        "minute": 0,
        "second": 0
    }

    rest_time = seconds
    for k, _ in time_dict.items():
        many_time, rest_time = convert(rest_time, k)
        time_dict[k] = many_time

    final_string = []
    for k, v in time_dict.items():
        string = generate_message(v, k)
        if string:
            final_string.append(string)

    return " and ".join([", ".join(final_string[:-1]), final_string[-1]] if len(final_string) > 2 else final_string)


if __name__ == "__main__":
    print(format_duration(0))  # "now"
    print(format_duration(1))  # "1 second"
    print(format_duration(62))  # "1 minute and 2 seconds"
    print(format_duration(120))  # "2 minutes"
    print(format_duration(3600))  # "1 hour"
    print(format_duration(3662))  # "1 hour, 1 minute and 2 seconds"
