"""base

Revision ID: 74f15fe195b6
Revises: 
Create Date: 2023-07-26 10:40:38.417139

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '74f15fe195b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_states',
    sa.Column('hash', sa.String(), nullable=False),
    sa.Column('account', sa.String(), nullable=True),
    sa.Column('balance', sa.BigInteger(), nullable=True),
    sa.Column('account_status', sa.Enum('uninit', 'frozen', 'active', name='account_status_type'), nullable=True),
    sa.Column('frozen_hash', sa.String(), nullable=True),
    sa.Column('code_hash', sa.String(), nullable=True),
    sa.Column('data_hash', sa.String(), nullable=True),
    sa.Column('code_boc', sa.String(), nullable=True),
    sa.Column('data_boc', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('hash')
    )
    op.create_table('blocks',
    sa.Column('workchain', sa.Integer(), nullable=False),
    sa.Column('shard', sa.BigInteger(), nullable=False),
    sa.Column('seqno', sa.Integer(), nullable=False),
    sa.Column('root_hash', sa.String(length=44), nullable=True),
    sa.Column('file_hash', sa.String(length=44), nullable=True),
    sa.Column('mc_block_workchain', sa.Integer(), nullable=True),
    sa.Column('mc_block_shard', sa.BigInteger(), nullable=True),
    sa.Column('mc_block_seqno', sa.Integer(), nullable=True),
    sa.Column('global_id', sa.Integer(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('after_merge', sa.Boolean(), nullable=True),
    sa.Column('before_split', sa.Boolean(), nullable=True),
    sa.Column('after_split', sa.Boolean(), nullable=True),
    sa.Column('want_split', sa.Boolean(), nullable=True),
    sa.Column('key_block', sa.Boolean(), nullable=True),
    sa.Column('vert_seqno_incr', sa.Boolean(), nullable=True),
    sa.Column('flags', sa.Integer(), nullable=True),
    sa.Column('gen_utime', sa.BigInteger(), nullable=True),
    sa.Column('start_lt', sa.BigInteger(), nullable=True),
    sa.Column('end_lt', sa.BigInteger(), nullable=True),
    sa.Column('validator_list_hash_short', sa.Integer(), nullable=True),
    sa.Column('gen_catchain_seqno', sa.Integer(), nullable=True),
    sa.Column('min_ref_mc_seqno', sa.Integer(), nullable=True),
    sa.Column('prev_key_block_seqno', sa.Integer(), nullable=True),
    sa.Column('vert_seqno', sa.Integer(), nullable=True),
    sa.Column('master_ref_seqno', sa.Integer(), nullable=True),
    sa.Column('rand_seed', sa.String(length=44), nullable=True),
    sa.Column('created_by', sa.String(), nullable=True),
    sa.Column('tx_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mc_block_workchain', 'mc_block_shard', 'mc_block_seqno'], ['blocks.workchain', 'blocks.shard', 'blocks.seqno'], ),
    sa.PrimaryKeyConstraint('workchain', 'shard', 'seqno')
    )
    op.create_table('jetton_masters',
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('total_supply', sa.Numeric(), nullable=True),
    sa.Column('mintable', sa.Boolean(), nullable=True),
    sa.Column('admin_address', sa.String(), nullable=True),
    sa.Column('jetton_content', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('jetton_wallet_code_hash', sa.String(), nullable=True),
    sa.Column('code_hash', sa.String(), nullable=True),
    sa.Column('data_hash', sa.String(), nullable=True),
    sa.Column('last_transaction_lt', sa.BigInteger(), nullable=True),
    sa.Column('code_boc', sa.String(), nullable=True),
    sa.Column('data_boc', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('address')
    )
    op.create_table('jetton_wallets',
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('balance', sa.Numeric(), nullable=True),
    sa.Column('owner', sa.String(), nullable=True),
    sa.Column('jetton', sa.String(), nullable=True),
    sa.Column('last_transaction_lt', sa.BigInteger(), nullable=True),
    sa.Column('code_hash', sa.String(), nullable=True),
    sa.Column('data_hash', sa.String(), nullable=True),
    sa.Column('code_boc', sa.String(), nullable=True),
    sa.Column('data_boc', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('address')
    )
    op.create_table('message_contents',
    sa.Column('hash', sa.String(length=44), nullable=False),
    sa.Column('body', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('hash')
    )
    op.create_table('messages',
    sa.Column('hash', sa.String(length=44), nullable=False),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('destination', sa.String(), nullable=True),
    sa.Column('value', sa.BigInteger(), nullable=True),
    sa.Column('fwd_fee', sa.BigInteger(), nullable=True),
    sa.Column('ihr_fee', sa.BigInteger(), nullable=True),
    sa.Column('created_lt', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.BigInteger(), nullable=True),
    sa.Column('opcode', sa.Integer(), nullable=True),
    sa.Column('ihr_disabled', sa.Boolean(), nullable=True),
    sa.Column('bounce', sa.Boolean(), nullable=True),
    sa.Column('bounced', sa.Boolean(), nullable=True),
    sa.Column('import_fee', sa.BigInteger(), nullable=True),
    sa.Column('body_hash', sa.String(length=44), nullable=True),
    sa.Column('init_state_hash', sa.String(length=44), nullable=True),
    sa.PrimaryKeyConstraint('hash')
    )
    op.create_table('nft_collections',
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('next_item_index', sa.Numeric(), nullable=True),
    sa.Column('owner_address', sa.String(), nullable=True),
    sa.Column('collection_content', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('data_hash', sa.String(), nullable=True),
    sa.Column('code_hash', sa.String(), nullable=True),
    sa.Column('last_transaction_lt', sa.BigInteger(), nullable=True),
    sa.Column('code_boc', sa.String(), nullable=True),
    sa.Column('data_boc', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('address')
    )
    op.create_table('nft_items',
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('init', sa.Boolean(), nullable=True),
    sa.Column('index', sa.Numeric(), nullable=True),
    sa.Column('collection_address', sa.String(), nullable=True),
    sa.Column('owner_address', sa.String(), nullable=True),
    sa.Column('content', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('last_transaction_lt', sa.BigInteger(), nullable=True),
    sa.Column('code_hash', sa.String(), nullable=True),
    sa.Column('data_hash', sa.String(), nullable=True),
    sa.Column('code_boc', sa.String(), nullable=True),
    sa.Column('data_boc', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('address')
    )
    op.create_table('transactions',
    sa.Column('block_workchain', sa.Integer(), nullable=True),
    sa.Column('block_shard', sa.BigInteger(), nullable=True),
    sa.Column('block_seqno', sa.Integer(), nullable=True),
    sa.Column('account', sa.String(), nullable=True),
    sa.Column('hash', sa.String(), nullable=False),
    sa.Column('lt', sa.BigInteger(), nullable=True),
    sa.Column('prev_trans_hash', sa.String(), nullable=True),
    sa.Column('prev_trans_lt', sa.BigInteger(), nullable=True),
    sa.Column('now', sa.Integer(), nullable=True),
    sa.Column('orig_status', sa.Enum('uninit', 'frozen', 'active', 'nonexist', name='account_status'), nullable=True),
    sa.Column('end_status', sa.Enum('uninit', 'frozen', 'active', 'nonexist', name='account_status'), nullable=True),
    sa.Column('total_fees', sa.BigInteger(), nullable=True),
    sa.Column('account_state_hash_before', sa.String(), nullable=True),
    sa.Column('account_state_hash_after', sa.String(), nullable=True),
    sa.Column('description', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.ForeignKeyConstraint(['block_workchain', 'block_shard', 'block_seqno'], ['blocks.workchain', 'blocks.shard', 'blocks.seqno'], ),
    sa.PrimaryKeyConstraint('hash')
    )
    op.create_table('jetton_burns',
    sa.Column('transaction_hash', sa.String(), nullable=False),
    sa.Column('query_id', sa.Numeric(), nullable=True),
    sa.Column('owner', sa.String(), nullable=True),
    sa.Column('jetton_wallet_address', sa.String(), nullable=True),
    sa.Column('amount', sa.Numeric(), nullable=True),
    sa.Column('response_destination', sa.String(), nullable=True),
    sa.Column('custom_payload', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['transaction_hash'], ['transactions.hash'], ),
    sa.PrimaryKeyConstraint('transaction_hash')
    )
    op.create_table('jetton_transfers',
    sa.Column('transaction_hash', sa.String(), nullable=False),
    sa.Column('query_id', sa.Numeric(), nullable=True),
    sa.Column('amount', sa.Numeric(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('destination', sa.String(), nullable=True),
    sa.Column('jetton_wallet_address', sa.String(), nullable=True),
    sa.Column('response_destination', sa.String(), nullable=True),
    sa.Column('custom_payload', sa.String(), nullable=True),
    sa.Column('forward_ton_amount', sa.Numeric(), nullable=True),
    sa.Column('forward_payload', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['transaction_hash'], ['transactions.hash'], ),
    sa.PrimaryKeyConstraint('transaction_hash')
    )
    op.create_table('nft_transfers',
    sa.Column('transaction_hash', sa.String(), nullable=False),
    sa.Column('query_id', sa.Numeric(), nullable=True),
    sa.Column('nft_item_address', sa.String(), nullable=True),
    sa.Column('old_owner', sa.String(), nullable=True),
    sa.Column('new_owner', sa.String(), nullable=True),
    sa.Column('response_destination', sa.String(), nullable=True),
    sa.Column('custom_payload', sa.String(), nullable=True),
    sa.Column('forward_amount', sa.Numeric(), nullable=True),
    sa.Column('forward_payload', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['transaction_hash'], ['transactions.hash'], ),
    sa.PrimaryKeyConstraint('transaction_hash')
    )
    op.create_table('transaction_messages',
    sa.Column('transaction_hash', sa.String(length=44), nullable=False),
    sa.Column('message_hash', sa.String(length=44), nullable=False),
    sa.Column('direction', sa.Enum('in', 'out', name='direction'), nullable=False),
    sa.ForeignKeyConstraint(['transaction_hash'], ['transactions.hash'], ),
    sa.PrimaryKeyConstraint('transaction_hash', 'message_hash', 'direction')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction_messages')
    op.drop_table('nft_transfers')
    op.drop_table('jetton_transfers')
    op.drop_table('jetton_burns')
    op.drop_table('transactions')
    op.drop_table('nft_items')
    op.drop_table('nft_collections')
    op.drop_table('messages')
    op.drop_table('message_contents')
    op.drop_table('jetton_wallets')
    op.drop_table('jetton_masters')
    op.drop_table('blocks')
    op.drop_table('account_states')
    # ### end Alembic commands ###
