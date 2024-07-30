from alembic import op
import sqlalchemy as sa

revision = '2'
down_revision = "1"
branch_labels = None
depends_on = None

def upgrade():
    with open('/app/app/alembic/seed/inserts.sql', 'r') as file:
        sql = file.read()
    op.execute(sql)

def downgrade():
    op.execute('DELETE FROM taxi;')