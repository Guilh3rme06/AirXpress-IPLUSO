def trimmer(*args):
    return tuple(s.strip() if isinstance(s, str) else s for s in args)