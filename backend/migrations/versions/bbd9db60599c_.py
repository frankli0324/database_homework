"""empty message

Revision ID: bbd9db60599c
Revises: e3fc939cf1c5
Create Date: 2020-07-30 17:28:25.730514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbd9db60599c'
down_revision = 'e3fc939cf1c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('min_compulsory_credit', sa.Integer(), nullable=True),
    sa.Column('min_elective_credit', sa.Integer(), nullable=True),
    sa.Column('min_limited_credit', sa.Integer(), nullable=True),
    sa.Column('max_compulsory_fail_credit', sa.Integer(), nullable=True),
    sa.Column('max_elective_fail_credit', sa.Integer(), nullable=True),
    sa.Column('max_limited_fail_credit', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('subject', sa.Column('schedule_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'subject', 'schedule', ['schedule_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subject', type_='foreignkey')
    op.drop_column('subject', 'schedule_id')
    op.drop_table('schedule')
    # ### end Alembic commands ###
