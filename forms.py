from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Titulo del Post", validators=[DataRequired()])
    subtitle = StringField("Subtitulo", validators=[DataRequired()])
    img_url = StringField("URL de Imagen del Post", validators=[DataRequired(), URL()])
    body = CKEditorField("Contenido del Post", validators=[DataRequired()])
    submit = SubmitField("Postear")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Nombre", validators=[DataRequired()])
    submit = SubmitField("Anotame!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Quiero Entrar!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Enviar comentario")
