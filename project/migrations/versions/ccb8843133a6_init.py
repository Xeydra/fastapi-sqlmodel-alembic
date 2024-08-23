"""init

Revision ID: ccb8843133a6
Revises: 166b7233ca79
Create Date: 2024-08-23 09:12:13.942367

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel             # NEW


# revision identifiers, used by Alembic.
revision = 'ccb8843133a6'
down_revision = '166b7233ca79'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userquestioncolorlink',
    sa.Column('user_question_id', sa.Integer(), nullable=False),
    sa.Column('color_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['color_id'], ['color.id'], ),
    sa.ForeignKeyConstraint(['user_question_id'], ['userquestioncolor.id'], ),
    sa.PrimaryKeyConstraint('user_question_id', 'color_id')
    )
    op.drop_table('userquestionanswersetlinkcolor')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userquestionanswersetlinkcolor',
    sa.Column('user_question_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('color_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['color_id'], ['color.id'], name='userquestionanswersetlinkcolor_color_id_fkey'),
    sa.ForeignKeyConstraint(['user_question_id'], ['userquestioncolor.id'], name='userquestionanswersetlinkcolor_user_question_id_fkey'),
    sa.PrimaryKeyConstraint('user_question_id', 'color_id', name='userquestionanswersetlinkcolor_pkey')
    )
    op.drop_table('userquestioncolorlink')
    # ### end Alembic commands ###
