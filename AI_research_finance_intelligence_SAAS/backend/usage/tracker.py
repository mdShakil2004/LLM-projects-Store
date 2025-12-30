from .limiter import check_limit

def track_usage(user, tokens=1):
    check_limit(user)
    user.credits -= tokens
