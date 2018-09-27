def construct(idordomain):
    if idordomain.isdigit():
        return(('owner_id', idordomain))
    else:
        return(('domain', idordomain))


def url(page):
    _tmp = construct(page)
    return(
        _tmp[0] +
        '=' +
        _tmp[1]
    )
