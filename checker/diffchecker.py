from difflib import Differ

differ = Differ()


def chunks(lst, n):
    l = []
    for i in range(0, len(lst), n):
        l.append(lst[i : i + n])
    return l


def make_lines_equals(l, r):
    max_length = max(len(l), len(r))
    l += [""] * (max_length - len(l))
    r += [""] * (max_length - len(r))


def check_diff(l, r):
    left, right = [], []
    print(l, r)
    for li, ri in zip(l, r):
        print("li:", r"{}".format(li))
        print("ri:", r"{}".format(ri))

        li = "­" if li == "\r" else li
        ri = "­" if ri == "\r" else ri

        if li == ri:
            right.append("<div>" + li or ri + "</div>")
            left.append("<div>" + li or ri + "</div>")

        else:
            if ri and not li:
                left.append("<div class='red'>" + li + "</div>")
                right.append("<div class='grey'>­</div>")
            elif li and not ri:
                right.append("<div class='red'>" + li + "</div>")
                left.append("<div class='grey'>­</div>")
            else:
                differance = list(differ.compare(li, ri))
                print(differance)
                right.append(
                    "<div class='red'>{}</div>".format(
                        span_it(differance, "- ", "lost")
                    )
                )
                left.append(
                    "<div class='green'>{}</div>".format(
                        span_it(differance, "+ ", "new")
                    )
                )

    return left, right


def span_it(_list, start, _class):
    filter_start = "- " if start == "+ " else "+ "
    _list = list(filter(lambda x: not x.startswith(filter_start), _list))
    temp_list = list()
    string_result = ""
    for char in _list:
        if char.startswith(start):
            temp_list.append(char[2:])
        else:
            if len(temp_list) > 0:
                string_result += "<span class='{}'>{}</span>".format(
                    _class, "".join(temp_list)
                )
                temp_list.clear()
            string_result += char[2:]

    if len(temp_list) > 0:
        string_result += "<span class='{}'>{}</span>".format(_class, "".join(temp_list))
    return string_result

