from wtforms import Form, StringField, validators, FileField


class AccountSettingsForm(Form):
    name = StringField('Username', [validators.Length(min=4, max=120)])
    avatar = FileField('Avatar Image')
