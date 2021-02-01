from pprint import pprint

black_wins = {'WIN': {(): False}, 'LOSE': {(): True}, None: {}}


def normalize(kaki):
    return [x for x in sorted(kaki) if x > 0]


def next_kaki(rule, kaki):
    kaki = normalize(kaki)
    if rule is None:
        yield "WIN", kaki[:]
        yield "LOSE", kaki[:]
    for i, x in enumerate(kaki):
        while kaki[i] > 0:
            kaki[i] -= 1
            yield rule, normalize(kaki)
        kaki[i] = x


def black(rule, kaki):
    kaki = normalize(kaki)
    kakit = tuple(kaki)
    if kakit in black_wins[rule]: return black_wins[rule][kakit]
    result = True
    for nrule, nkaki in next_kaki(rule, kaki):
        nkakit = tuple(nkaki)
        black_wins[nrule][nkakit] = black(nrule, nkaki)
        result = result and black_wins[nrule][nkakit]
    black_wins[rule][kakit] = not result
    return black_wins[rule][kakit]


def next_hand(rule, kaki):
    kaki = normalize(kaki)
    result = []
    if not black(rule, kaki):
        return []
    for nrule, nkaki in next_kaki(rule, kaki):
        if not black(nrule, nkaki):
            result.append((nrule, tuple(nkaki)))
    return result


if __name__ == '__main__':
    WIN = "WIN"
    LOSE = "LOSE"
    while True:
        temp = input().split()
        rule, kaki = temp[0], list(map(int, temp[1:]))
        if rule == 'w':
            rule = WIN
        elif rule == 'l':
            rule = LOSE
        else:
            rule = None
        print(rule, kaki)
        print(next_hand(rule, kaki))
        # pprint(black_wins)
