from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e3847ccc4816'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'fastapi',
        sa.Column('Sn', sa.Integer(), primary_key=True),
        sa.Column('Symbol', sa.String(length=50), nullable=False),
        sa.Column('Close_Price_Rs', sa.Float(), nullable=True),
        sa.Column('Open_Price_Rs', sa.Float(), nullable=True),
        sa.Column('High_Price_Rs', sa.Float(), nullable=True),
        sa.Column('Low_Price_Rs', sa.Float(), nullable=True),
        sa.Column('Total_Traded_Quantity', sa.Integer(), nullable=True),
        sa.Column('Total_Traded_Value', sa.Float(), nullable=True),
        sa.Column('Total_Trades', sa.Integer(), nullable=True),
        sa.Column('LTP', sa.Float(), nullable=True),
        sa.Column('Previous_Day_Close_Price_Rs', sa.Float(), nullable=True),
        sa.Column('Average_Traded_Price_Rs', sa.Float(), nullable=True),
        sa.Column('Fifty_Two_Week_High_Rs', sa.Float(), nullable=True),
        sa.Column('Fifty_Two_Week_Low_Rs', sa.Float(), nullable=True),
        sa.Column('Market_Capitalization_Rs__Amt_in_Millions', sa.Float(), nullable=True),
        sa.Column('Close_Date', sa.Date(), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('fastapi')
