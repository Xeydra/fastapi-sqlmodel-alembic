"""seed_color_questions

Revision ID: c829e703d7d7
Revises: bef2f68e0ec4
Create Date: 2024-08-29 08:00:42.848993

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel             # NEW
from sqlalchemy.orm import Session
from app.models import AnswerSetColor, UserQuestionColor


# revision identifiers, used by Alembic.
revision = 'c829e703d7d7'
down_revision = 'bef2f68e0ec4'
branch_labels = None
depends_on = None



def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    colors = [
        AnswerSetColor(label='Weiß', value='#FFFFFF'),
        AnswerSetColor(label='Schwarz', value='#000000'),
        AnswerSetColor(label='Rot', value='#FF0000'),
        AnswerSetColor(label='Gelb', value='#FFFF00'),
        AnswerSetColor(label='Grün', value='#00FF00'),
        AnswerSetColor(label='Blau', value='#0000FF'),
        AnswerSetColor(label='Magenta', value='#FF00FF'),
    ]
    
    session.add_all(colors)
    session.commit()
    
    userQuestion = UserQuestionColor(question_text="Wie fühlst du dich heute?")

    colors = session.execute(sa.select(AnswerSetColor)).scalars().all()
    userQuestion.answer_set = colors
    session.add(userQuestion)
    session.commit()
    session.close()
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    session = Session(bind=bind)
    session.query(UserQuestionColor).delete()
    session.query(AnswerSetColor).delete()
    session.commit()
    pass
    # ### end Alembic commands ###
