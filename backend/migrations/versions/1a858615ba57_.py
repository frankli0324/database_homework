"""empty message

Revision ID: 1a858615ba57
Revises: bbd9db60599c
Create Date: 2020-07-30 17:39:46.390447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a858615ba57'
down_revision = 'bbd9db60599c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('score',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_try', sa.Integer(), nullable=True),
    sa.Column('second_try', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'student', ['studentNum'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='unique')
    op.drop_table('score')
    # ### end Alembic commands ###
