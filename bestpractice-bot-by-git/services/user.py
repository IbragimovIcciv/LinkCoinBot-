
from models.user import User


async def add_user(tg_id: int, full_name: str, username: str, referred_by_code: str = None):
    referral_code = await User.generate_unique_referral_code()

    user = User(
        tg_id=tg_id,
        full_name=full_name,
        username=username,
        referral_code=referral_code,
        referred_by=None
    )

    if referred_by_code:
        referrer = await User.get_or_none(referral_code=referred_by_code)
        if referrer:
            user.referred_by = referrer
            referrer.referral_count += 1
            referrer.balance += 10
            await referrer.save()

    await user.save()


async def get_user(tg_id: int):
    user = await User.get_or_none(tg_id=tg_id)
    return user


async def check_address(token: str):
    user = await User.get_or_none(referral_code=token)
    return user
