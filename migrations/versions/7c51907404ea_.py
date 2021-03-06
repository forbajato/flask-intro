"""empty message

Revision ID: 7c51907404ea
Revises: 
Create Date: 2017-08-22 16:14:02.028289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c51907404ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kickoff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('papresults',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('patientNumber', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('lmp', sa.String(), nullable=True),
    sa.Column('adequateSample', sa.Boolean(), nullable=False),
    sa.Column('cellCount', sa.Integer(), nullable=False),
    sa.Column('endocervicalCells', sa.Boolean(), nullable=False),
    sa.Column('metaplasticCells', sa.Boolean(), nullable=False),
    sa.Column('backgroundInflammation', sa.String(), nullable=False),
    sa.Column('fungal', sa.Boolean(), nullable=False),
    sa.Column('trich', sa.Boolean(), nullable=False),
    sa.Column('hpv', sa.Boolean(), nullable=False),
    sa.Column('bacteria', sa.Boolean(), nullable=False),
    sa.Column('hsv', sa.Boolean(), nullable=False),
    sa.Column('impression', sa.String(), nullable=False),
    sa.Column('advice', sa.String(), nullable=False),
    sa.Column('doctor', sa.String(), nullable=False),
    sa.Column('disposition', sa.String(), nullable=False),
    sa.Column('kickoff_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['kickoff_id'], ['kickoff.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('papresults')
    op.drop_table('kickoff')
    # ### end Alembic commands ###
