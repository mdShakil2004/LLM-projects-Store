def check_limit(user):
    if user.plan == "free" and user.credits <= 0:
        raise Exception("Upgrade required")
