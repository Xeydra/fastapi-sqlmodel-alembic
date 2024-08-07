"""init_tables

Revision ID: e78b1e2af183
Revises: 
Create Date: 2024-08-01 08:21:17.770288

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel             # NEW


# revision identifiers, used by Alembic.
revision = 'e78b1e2af183'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questiontype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tech_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_questiontype_tech_id'), 'questiontype', ['tech_id'], unique=True)
    op.create_table('userquestion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_text', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('question_type_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['question_type_id'], ['questiontype.tech_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userdatacolor',
    sa.Column('value', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('for_date', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('user_question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_question_id'], ['userquestion.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userdatacolor')
    op.drop_table('userquestion')
    op.drop_index(op.f('ix_questiontype_tech_id'), table_name='questiontype')
    op.drop_table('questiontype')
    # ### end Alembic commands ###
