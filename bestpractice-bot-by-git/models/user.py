from tortoise import fields
from tortoise.models import Model
import uuid


class User(Model):
    id = fields.IntField(pk=True)
    tg_id = fields.BigIntField(unique=True)
    full_name = fields.CharField(max_length=255, null=True)
    username = fields.CharField(max_length=255, unique=True)
    balance = fields.IntField(default=0, null=True)
    referral_code = fields.CharField(max_length=36, unique=True)
    referral_count = fields.IntField(default=0)
    referred_by = fields.ForeignKeyField("models.User", related_name="referrals", null=True)

    class Meta:
        table = "users"

    @classmethod
    async def generate_unique_referral_code(cls):
        while True:
            referral_code = str(uuid.uuid4())
            if not await cls.filter(referral_code=referral_code).exists():
                return referral_code


class Transaction(Model):
    id = fields.IntField(pk=True)
    sender = fields.ForeignKeyField("models.User", related_name="sender_transactions", null=True)
    receiver = fields.ForeignKeyField("models.User", related_name="receiver_transactions", null=True)
    amount = fields.IntField(null=True)
    timestamp = fields.DatetimeField(auto_now_add=True)
    note = fields.CharField(max_length=255)

    @classmethod
    async def create_transaction(cls, sender: User, receiver: User, amount: int, note: str = None):
        if sender.balance < amount:
            raise ValueError("sender balance must be greater than receiver balance")
        sender.balance -= amount
        receiver.balance += amount
        await sender.save()
        await receiver.save()
        await cls.create(sender=sender, receiver=receiver, amount=amount, note=note)