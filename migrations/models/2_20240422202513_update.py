from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `todo` (
    `id` CHAR(36) NOT NULL  PRIMARY KEY,
    `title` VARCHAR(100) NOT NULL,
    `done` BOOL NOT NULL  DEFAULT 0,
    `create_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `todo`;"""
